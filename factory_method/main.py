# Python 3.9 or higher due to type hint support
import json
import xml.etree.ElementTree as etree
from typing import Union, Optional

class JSONDataExtractor:
    def __init__(self, filepath: str):
        self._data = {}
        with open(filepath, mode="r", encoding="utf-8") as f:
            self._data = json.load(f)

    @property
    def parsed_data(self) -> Union[dict,list]:
        return self._data

class XMLDataExtractor:
    def __init__(self,filepath: str):
        self._tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self._tree

ExtractorFactory = Union[
        JSONDataExtractor,
        XMLDataExtractor
        ]

def data_extraction_factory(filepath: str) -> ExtractorFactory:
    if filepath.endswith('.json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('.xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f"Cannot parse data from {filepath}")
    return extractor(filepath)

def extract_data_from(filepath: str) -> Optional[ExtractorFactory]:
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj

def main():
    sqlite_factory = extract_data_from('db.sqlite3')
    print()
    json_factory = extract_data_from('movies.json')
    json_data = json_factory.parsed_data
    print(f"Found {len(json_data)} movie(s)")

    for movie in json_data:
        print(f"Title: {movie['title']}")
        year = movie["year"]
        if year:
            print(f"Year: {year}")
        director = movie["director"]
        if director:
            print(f"Director: {director}")
        genre = movie["genre"]
        if genre:
            print(f"Genre: {genre}")
        print()

    print()

    xml_factory = extract_data_from("person.xml")
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f"Found: {len(liars)} person(s)")
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f"Firstname: {firstname}")
        lastname = liar.find("lastName").text
        print(f"Lastname: {lastname}")
        [print(f"Phone number: ({p.attrib['type']}):{p.text}") for p in liar.find("phoneNumbers")]
        print()


if __name__ == "__main__":
    main()
