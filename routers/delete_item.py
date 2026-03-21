

def delete_item(request: Item, current_user: User=Depends(get_active_user), db: Session=Depends(get_db)):
  item_to_delete = db.query(models.Items).filter(models.Items.item = request.item).first()
  if not item_to_delete:
    raise HTTPException(status_code=404, detail="item not found")
  db.delete(item_to_delete)
  db.commit()
  return {
    "message": "done"
  }
  
