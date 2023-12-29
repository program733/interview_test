from lxml import etree
import json

def read_xml(xml_file_path):
    tree = etree.parse(xml_file_path)
    root = tree.getroot()
    return root

def update_xml_table(xml_root, sheet_name, json_data):
    ns = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

    # Find the specified sheet by name
    sheet = xml_root.find(".//ss:Worksheet[@ss:Name='{}']".format(sheet_name), namespaces=ns)

    if sheet is not None:
        # Find the table within the sheet
        table = sheet.find(".//ss:Table", namespaces=ns)

        if table is not None:
            # Update table columns based on JSON data
            for column in table.findall(".//ss:Cell/ss:Data", namespaces=ns):
                column_name = column.text
                if column_name in json_data:
                    # Update the column value from JSON data
                    column.getparent().find(".//ss:Cell/ss:Data", namespaces=ns).text = str(json_data[column_name])

def write_xml(xml_root, output_file):
    tree = etree.ElementTree(xml_root)
    tree.write(output_file, pretty_print=True, xml_declaration=True, encoding='utf-8')

def main():
    # Path to the XML file
    xml_file_path = 'worksheet.xml'

    # Path to the JSON file
    json_file_path = 'data.json'

    # Sheet name to update
    sheet_name = 'Sheet1'

    # Read XML
    xml_root = read_xml(xml_file_path)

    # Read JSON
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Update XML table based on sheet name and JSON data
    update_xml_table(xml_root, sheet_name, json_data)

    # Write modified XML to a new file
    output_file_path = 'output_modified.xml'
    write_xml(xml_root, output_file_path)

if __name__ == "__main__":
    main()
