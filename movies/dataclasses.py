from dataclasses import dataclass

@dataclass
class PersonPreviewDataClass:
    id:int
    name:str
    enName:str
    description:str=''
    photoURL:str='https://sh72-lipeck-r42.gosweb.gosuslugi.ru/netcat_files/11/145/20200701_001_6.jpg'

@dataclass
class MoviePreviewDataClass:
    id:int
    name:str
    year: str='1970'
    ageRating:str='0+'
    posterURL: str='https://newsrnd.com/images/no-image.png'
    ratingIMDB:float=0
    premiereDate: str='Jan 1 1970'


@dataclass
class MovieDetailDataClass:
    kpid:int
    name:str
    type:str
    ratingIMDB: float
    ratingKP: float
    year: str
    ageRating:str
    description:str

    backdropURL:str
    posterURL:str
    trailerURL: str

@dataclass
class WatchabilityItem:
    name:str
    logoURL:str
    URL:str







