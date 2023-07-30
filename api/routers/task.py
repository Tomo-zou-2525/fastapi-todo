from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

# ルーターでは、スキーマ側で定義したものを利用してAPIのリクエストとレスポンスを定義
router = APIRouter()

# Taksのリスト閲覧
# @router.get("/tasks")
# async def list_tasks():
#     pass
@router.get("/tasks", response_model=List[task_schema.Task])
# response_modelをListで返すのは、Taskの応答が複数であるから
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTODOタスク")]
    # これはダミーデータ

# タスクの追加
@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())
    """
    リクエストに対してレスポンスデータは id を持つ
    リクエストボディのクラス task_schema.TaskCreate をいったん dict に変換
    これらのkey/valueおよび id=1 を持つ task_schema.TaskCreateResponse インスタンスを作成
    これが task_schema.TaskCreateResponse(id=1, **task_body.dict())
    """
    """
    dict インスタンスに対して先頭に ** をつけることで、 dict を キーワード引数として展開
    task_schema.TaskCreateResponse クラスのコンストラクタに対して dict のkey/valueを渡す
    つまり、task_schema.TaskCreateResponse(id=1, title=task_body.title, done=task_body.done)と同値
    """

# タスクの更新
@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_body: task_schema.TaskCreateResponse):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

# タスクの削除
@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return