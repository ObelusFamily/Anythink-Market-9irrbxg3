from typing import List, Optional

from pydantic import validator

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.rwmodel import RWModel


class Item(IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    tags: List[str]
    seller: Profile
    favorited: bool
    favorites_count: int
    image: Optional[str]
    body: Optional[str]

    @validator('image', pre=True, always=True)
    def set_default_image(cls, v):
        return v or '/placeholder.png'
