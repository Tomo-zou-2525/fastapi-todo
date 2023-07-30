from typing import Optional

from pydantic import BaseModel, Field

# APIのスキーマ定義を作成
class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="Unko")
    done: bool = Field(False, description="完了フラグ")

# develop push test