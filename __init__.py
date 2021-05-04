import string
from datetime import date
from typing import List

class ResourceList:
    returned: int
    collectionURI: string
    items: List

class CoreResource:
    id: int
    name: string
    description: string
    modified: date
    resourceURI: string
    urls: List[Url]
    thumbnail: Image
    comics: ResourceList
    stories: ResourceList
    events: ResourceList
    series: ResourceList
