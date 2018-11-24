import logging
import xml.etree.ElementTree as ET

logging.basicConfig(level=logging.DEBUG)
file_name = "resources/bsp-001_1975_081_0001.xml"
namespace = "{http://www.abbyy.com/FineReader_xml/FineReader10-schema-v1.xml}"
font_size_attribute_name = "fs"
headline_font_size = "34"
new_line_char = "\n"
page_counter = 0

def get_formatting_elements_with_headlines(element):
  formatting_element_path = ".//{0}par/{0}line/{0}formatting[@fs='{1}.']" \
      .format(namespace, headline_font_size)
  return element.findall(formatting_element_path)

def contains_headline(page_element):
  formatting_elements = get_formatting_elements_with_headlines(page_element)
  return len(formatting_elements) > 0

def remove_non_headline_elements(text_element):
  line_element_path = ".//{0}par/{0}line".format(namespace)
  line_elements = text_element.findall(line_element_path)

  for line_element in line_elements:
    formatting_elements = list(line_element) # get all children of the "line" element

    for element in formatting_elements:
      fontSize = element.get(font_size_attribute_name)
      if fontSize != headline_font_size + ".":
        line_element.remove(element)

def get_letters_of_headline(text_element):
  isRelevantLetter = lambda text: new_line_char not in text
  filteredTextIter = filter(isRelevantLetter, text_element.itertext())
  return list(filteredTextIter)

# Main program flow

logging.info("Parsing the file '%s'", file_name)

tree = ET.parse(file_name)
root = tree.getroot()

# go through all pages and search for headlines
page_element_path = ".//{0}page".format(namespace)
all_page_elements = root.findall(page_element_path)

for page_element in all_page_elements:
  page_counter += 1
  if contains_headline(page_element):
    # get all text elements containing headline letters
    text_elementPath = ".//{0}block/{0}text".format(namespace)
    all_text_elements = page_element.findall(text_elementPath)
    filtered_text_elements = list(filter(contains_headline, all_text_elements))

    for element in filtered_text_elements:
      remove_non_headline_elements(element)
      headline_letters = get_letters_of_headline(element)
      headline_info = {
        "headline": "".join(headline_letters),
        "page": page_counter
      }
      logging.info(headline_info)
