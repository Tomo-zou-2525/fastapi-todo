from typing import Optional

from pydantic import BaseModel, Field

# APIのスキーマ定義を作成
# BaseModel はFastAPIのスキーマモデルであることを表す
# 右辺の Field はフィールドに関する付加情報を記述します。最初の変数はフィールドのデフォルト値を表します。 title は None 、 done は False をデフォルト値
class Task(BaseModel):
    id: int
    # title: Optional[str] = Field(None, example="Unko")
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    title: Optional[str] = Field(None, example="Tinko")
# develop push test

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True