from fastapi import APIRouter

router = APIRouter()

# Taksのリスト閲覧
@router.get("/tasks")
async def list_tasks():
    pass

# タスクの追加
@router.post("/tasks")
async def create_task():
    pass

# タスクの更新
@router.put("/tasks/{task_id}")
async def update_task():
    pass

# タスクの削除
@router.delete("/tasks/{task_id}")
async def delete_task():
    pass