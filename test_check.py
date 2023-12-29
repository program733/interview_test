import xml.etree.ElementTree as ET
import json

def read_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    return root

def update_xml_table(xml_root, sheet_name, json_data):
    # Find the specified sheet by name
    sheet = xml_root.find(".//Worksheet[@ss:Name='{}']".format(sheet_name), namespaces={'ss': 'urn:schemas-microsoft-com:office:spreadsheet'})

    if sheet is not None:
        # Find the table within the sheet
        table = sheet.find(".//Table", namespaces={'ss': 'urn:schemas-microsoft-com:office:spreadsheet'})

        if table is not None:
            # Update table columns based on JSON data
            for column in table.findall(".//Cell/Data", namespaces={'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}):
                column_name = column.text
                if column_name in json_data:
                    # Update the column value from JSON data
                    column.getparent().find(".//Cell/Data", namespaces={'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}).text = str(json_data[column_name])

def write_xml(xml_root, output_file):
    tree = ET.ElementTree(xml_root)
    tree.write(output_file)

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
