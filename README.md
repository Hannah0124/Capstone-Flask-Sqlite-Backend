# Capstone-Flask-Sqlite-Backend

Our Capstone project (Vizlator) is a Python + Flask + PostgreSQL API used with React Native App Frontend to save users profile & images.

## Routes

- **Retrieve all Users**
  - GET
  - `'/users'`
- **Create User**
  - POST
  - `'/add_user'`
- **Get all Images**
  - GET
  - `'/images/'`
- **Add an Image**
  - POST
  - `'/add_image'`
  - params: `{image_url, text, translated_text, language, user_id, original_lang }`
- **Remove an Image**
  - POST
  - `'/image/:id'`
 
