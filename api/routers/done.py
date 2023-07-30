from fastapi import APIRouter

router = APIRouter()

# Taksの実行フラグOn
@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done():
    return

# タスクの実行フラグOff
@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done():
    return