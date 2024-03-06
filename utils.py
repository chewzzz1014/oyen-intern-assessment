from db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_template(file_path, data):
    html_content = ''
    with open(file_path, 'r') as f:
        html_content = f.read().replace('USER', data['user'])
    if 'path' in data:
        html_content = html_content.replace('SELF_DEFINED_PATH', data['path'])
    return html_content