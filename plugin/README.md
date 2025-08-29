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
   python -m pip install aiohttp
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
                ├── add_task_comment/        # Plugin: Add comments to tasks
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_add_task_comment.py
                ├── add_task_watcher/        # Plugin: Add Watchers to members
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_add_task_watcher.py
                ├── assign_task/        # Plugin: Assign tasks for team members
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_assign_task.py
                ├── create_checklist/        # Plugin: Add checklists to tasks
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_create_checklist.py
                ├── create_list/             # Plugin: Create lists inside spaces/folders
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_create_list.py
                ├── create_space/        # Plugin: Create a new space
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_create_space.py
                ├── create_task/             # Plugin: Create new tasks
                │    ├── plugin.py           # Logic to call ClickUp Create Task API
                │    ├── plugin_schema.yml   # Schema: input/output definition
                │    └── test_create_task.py # Test script for plugin
                ├── delete_task/             # Plugin: Delete tasks
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_delete_task.py
                ├── get_custom_fields/        # Plugin: Retrieve available custom fields
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_get_custom_fields.py
                ├── get_lists/             # Plugin: Retrieve lists inside spaces/folders
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_get_lists.py
                ├── get_task/                # Plugin: Retrieve a single task
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_get_task.py
                ├── get_spaces/        # Plugin: List available spaces
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_get_spaces.py
                ├── get_time_entries/        # Plugin: Retrieve tracked time for tasks
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_get_time_entries.py
                ├── search_tasks/            # Plugin: Search tasks with filters
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_search_task.py
                ├── set_custom_field_value/        # Plugin: Update custom field values on tasks
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_set_custom_field_value.py
                ├── track_time/        # Plugin: Add tracked time entries to tasks
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_track_time.py
                ├── update_task/             # Plugin: Update task details
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_update_task.py
                ├── update_task_status/      # Plugin: Update only task status
                │    ├── plugin.py
                │    ├── plugin_schema.yml
                │    └── test_update_task_status.py

```

---

## 🔌 Plugins Overview

### 📝 Task Management
- **create_task** – Create a new task.
- **update_task**: Update existing task properties
- **delete_task**: Delete a task
- **search_tasks** – Search tasks by name, status, or ID.
- **get_task**: Retrieve detailed task information
- **add_task_comment** – Add comments to a task.
- **update_task_status** – Update status and name of tasks.

### 📂 List and Space Management
- **create_list**: Create a new list in a folder/space
- **get_lists** – Retrieve lists in a space.
- **create_space** – Create a new space in a team.
- **get_spaces** – Retrieve spaces for a team.

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
