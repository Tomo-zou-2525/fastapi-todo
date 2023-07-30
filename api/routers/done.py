from fastapi import APIRouter

router = APIRouter()

# Taksの実行フラグOn
@router.get("/tasks/{task_id}/done")
async def mark_task_as_done():
    pass

# タスクの実行フラグOff
@router.post("/tasks/{task_id}/done")
async def unmark_task_as_done():
    pass