# 🚀 ClickUp Plugin Suite

A collection of Python-based plugins to interact with the **ClickUp API**.  
This suite supports **task management, comments, spaces, lists, custom fields, time tracking, and team collaboration**.

---

## 📦 Features

- 📝 **Task Management**  
  Create, update, search, and manage tasks.
- 💬 **Comments**  
  Add and delete comments on tasks.
- 📂 **Spaces & Lists**  
  Manage spaces and lists in your ClickUp workspace.
- 🏷 **Custom Fields**  
  Retrieve and update task custom field values.
- ⏱ **Time Tracking**  
  Add tracked time and retrieve time entries.
- 👥 **Team Collaboration**  
  Assign tasks, add watchers, and create checklists.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pradeep-848/Clickup_Challenge.git
   cd Clickup_Challenge/plugin
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Authentication Setup

1. Log in to [ClickUp API Settings](https://app.clickup.com/settings/apps).  
2. Generate a **Personal API Token**.  
3. Store your token securely. You can pass it via environment variable or directly in tests:

```python
credentials = BundleCredentials(credentials={
    "CLICKUP_API_TOKEN": "your_api_token_here"
})
```

---

## 📂 Project Structure

```
plugin/
 └── bundles/
      └── clickup/
           ├── bundle_dependency.py          # Defines shared PluginInput, Output, and Credentials models
           ├── config.py                     # Configuration constants (e.g., proxy)
           ├── __init__.py                   # Marks directory as a Python package
           ├── shared/
           │    ├── __init__.py
           │    └── api_client.py            # Handles HTTP requests to ClickUp API (async with aiohttp)
           ├── resources/
           │    └── i18n/
           │         ├── en.yml              # Translations / localization support
           │         ├── bundle_schema.yml   # Defines schema for all plugins
           │         └── icon.png            # Bundle icon
           └── plugins/
                ├── create_task/             # Plugin: Create new tasks
                │    ├── plugin.py           # Logic to call ClickUp Create Task API
                │    ├── plugin_schema.yml   # Schema: input/output definition
                │    └── test_create_task.py # Test script for plugin
                ├── update_task/             # Plugin: Update task details
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_update_task.py
                ├── update_task_status/      # Plugin: Update only task status
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_update_task_status.py
                ├── delete_task/             # Plugin: Delete tasks
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_delete_task.py
                ├── get_task/                # Plugin: Retrieve a single task
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_get_task.py
                ├── search_tasks/            # Plugin: Search tasks with filters
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_search_task.py
                ├── create_list/             # Plugin: Create lists inside spaces/folders
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_create_list.py
                ├── add_task_comment/        # Plugin: Add comments to tasks
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_add_task_comment.py

```

---

## 🔌 Plugins Overview

### 📝 Task Management
- **create_task** – Create a new task.
- **update_task_status** – Update status and name of tasks.
- **search_tasks** – Search tasks by name, status, or ID.

### 💬 Comments
- **add_task_comment** – Add comments to a task.
- **delete_task_comment** – Delete a comment from a task.

### 📂 Spaces & Lists
- **create_space** – Create a new space in a team.
- **get_spaces** – Retrieve spaces for a team.
- **get_lists** – Retrieve lists in a space.

### 🏷 Custom Fields
- **get_custom_fields** – Retrieve available custom fields for a task.
- **set_custom_field_value** – Update a custom field value on a task.

### ⏱ Time Tracking
- **track_time** – Add tracked time entries to tasks.
- **get_time_entries** – Retrieve tracked time for tasks.

### 👥 Team Collaboration
- **assign_task** – Assign tasks to team members.
- **add_task_watcher** – Add watchers to tasks.
- **create_checklist** – Add checklists to tasks.

---

## 🧪 Example Usage

Each plugin comes with a test file. Example:

```bash
cd plugin/bundles/clickup/plugins/create_task
python test_create_task.py
```

---

## 🛠 Troubleshooting

- **401 Unauthorized** → Check your API token is valid and added correctly.  
- **400 Bad Request** → Ensure required parameters are provided (e.g., correct status, field IDs).  
- **404 Not Found** → Check task, list, or space ID exists.  
- **Time interval overlaps** → When tracking time, ensure `start` and `end` don’t overlap existing entries.

---

## 📜 License

This project is licensed under the MIT License.
