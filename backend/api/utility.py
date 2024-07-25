from internetarchive import get_item, search_items

class Utility:
  
  @staticmethod
  def format_metadata(item):
    meta = {}
    meta['identifier'] = item.metadata['identifier']
    meta['date'] = item.metadata.get('date', None)
    meta['language'] = item.metadata.get('language', None)
    meta['mediatype'] = item.metadata.get('mediatype', None)
    meta['title'] = item.metadata.get('title', None)
    meta['description'] = item.metadata.get('description', None)
    meta['collection'] = item.metadata.get('collection', None)
    meta['url'] = "https://archive.org/details/" + item.metadata['identifier']
    return meta
  
  @classmethod
  def get_meta_data(cls, MetaData):
    data = get_item(MetaData)
    formatted_meta = Utility.format_metadata(data)
    return formatted_meta
  
  @classmethod
  def search_archive(cls, search_term):
    identifier_list = []
    for i in search_items(search_term):
      identifier_list.append(i['identifier'])
    return identifier_list
