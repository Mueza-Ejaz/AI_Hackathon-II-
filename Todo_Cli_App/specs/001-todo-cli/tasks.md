# Implementation Tasks: Todo CLI Application

**Feature Branch**: `001-todo-cli`
**Created**: 2025-12-12
**Status**: Draft
**Plan**: `specs/001-todo-cli/plan.md`
**Spec**: `specs/001-todo-cli/spec.md`

## Summary

This document outlines the detailed, dependency-ordered tasks required to implement the Todo CLI Application. Tasks are organized into phases, starting with setup and foundational components, followed by dedicated phases for each user story based on priority, and concluding with polish and cross-cutting concerns. Each task is granular and includes specific file paths to facilitate independent implementation and testing.

## Task Checklist

### Phase 1: Setup

- [X] T001 Create `src/` directory at project root
- [X] T002 Create `tests/` directory at project root
- [X] T003 Create `src/__init__.py` to mark `src` as a Python package
- [X] T004 Create `tests/unit/` and `tests/integration/` directories
- [X] T005 Create `tests/unit/test_todo.py` for unit tests
- [X] T006 Create `tests/integration/test_cli.py` for integration tests

### Phase 2: Foundational Components

- [X] T007 Implement `Task` class in `src/todo.py` with `id`, `title`, `description`, `completed` attributes
- [X] T008 Implement `TodoApp` class in `src/todo.py` to manage tasks (in-memory list)
- [X] T009 Initialize `TodoApp` with an empty list of tasks and a task ID counter in `src/todo.py`

### Phase 3: User Story 1 - Add and View Tasks (P1)

**Goal**: Users can add new tasks and view a list of all tasks.
**Independent Test Criteria**: Tasks can be added and successfully displayed with correct details (ID, title, description, status).

- [X] T010 [US1] Implement `add_task(self, title, description=None)` method in `src/todo.py::TodoApp`
- [X] T011 [US1] Implement `get_all_tasks(self)` method in `src/todo.py::TodoApp` to return all tasks
- [X] T012 [P] [US1] Add unit tests for `TodoApp.add_task` in `tests/unit/test_todo.py`
- [X] T013 [P] [US1] Add unit tests for `TodoApp.get_all_tasks` in `tests/unit/test_todo.py`
- [X] T014 [US1] Implement main menu loop and 'Add Task' option in `src/todo.py`
- [X] T015 [US1] Implement 'View Tasks' option to display all tasks in `src/todo.py`
- [X] T016 [P] [US1] Add integration tests for 'Add Task' and 'View Tasks' via CLI in `tests/integration/test_cli.py`

### Phase 4: User Story 2 - Mark Task as Complete (P1)

**Goal**: Users can mark an existing task as complete.
**Independent Test Criteria**: An existing task can be marked complete, and its status correctly reflects this change when viewed.

- [X] T017 [US2] Implement `mark_task_complete(self, task_id)` method in `src/todo.py::TodoApp`
- [X] T018 [P] [US2] Add unit tests for `TodoApp.mark_task_complete` including edge cases (invalid ID) in `tests/unit/test_todo.py`
- [X] T019 [US2] Add 'Mark Task Complete' option to the main menu in `src/todo.py`
- [X] T020 [P] [US2] Add integration tests for 'Mark Task Complete' via CLI in `tests/integration/test_cli.py`

### Phase 5: User Story 3 - Update Task (P2)

**Goal**: Users can update the title and/or description of an existing task.
**Independent Test Criteria**: An existing task's title and/or description can be updated, and the changes are reflected when viewed.

- [X] T021 [US3] Implement `update_task(self, task_id, new_title=None, new_description=None)` method in `src/todo.py::TodoApp`
- [X] T022 [P] [US3] Add unit tests for `TodoApp.update_task` including edge cases (invalid ID, partial updates) in `tests/unit/test_todo.py`
- [X] T023 [US3] Add 'Update Task' option to the main menu in `src/todo.py`
- [X] T024 [P] [US3] Add integration tests for 'Update Task' via CLI in `tests/integration/test_cli.py`

### Phase 6: User Story 4 - Delete Task (P2)

**Goal**: Users can delete tasks that are no longer needed.
**Independent Test Criteria**: An existing task can be deleted and is no longer present in the task list.

- [X] T025 [US4] Implement `delete_task(self, task_id)` method in `src/todo.py::TodoApp`
- [X] T026 [P] [US4] Add unit tests for `TodoApp.delete_task` including edge cases (invalid ID) in `tests/unit/test_todo.py`
- [X] T027 [US4] Add 'Delete Task' option to the main menu in `src/todo.py`
- [X] T028 [P] [US4] Add integration tests for 'Delete Task' via CLI in `tests/integration/test_cli.py`

### Phase 7: Polish & Cross-Cutting Concerns

**Goal**: Enhance robustness, user experience, and code quality across the application.

- [X] T029 Implement robust input validation for all user inputs (e.g., integer IDs, non-empty titles) in `src/todo.py`
- [X] T030 Implement comprehensive error handling and user-friendly error messages for all CLI operations in `src/todo.py`
- [X] T031 Refine main menu display and navigation for improved user experience in `src/todo.py`
- [X] T032 Ensure overall PEP 8 compliance and code quality across `src/` and `tests/`
- [X] T033 Implement exit option in the main menu to gracefully terminate the application in `src/todo.py`

## Dependencies

The following table illustrates the completion order of user stories and their dependencies. All user stories are designed to be largely independent once foundational components are in place.

| User Story                        | Depends On                               |
|-----------------------------------|------------------------------------------|
| User Story 1 (Add & View)         | Phase 2 (Foundational Components)        |
| User Story 2 (Mark Complete)      | Phase 3 (User Story 1 - to view status) |
| User Story 3 (Update Task)        | Phase 3 (User Story 1 - to view changes) |
| User Story 4 (Delete Task)        | Phase 3 (User Story 1 - to verify deletion) |
| Phase 7 (Polish & Cross-Cutting)  | All User Story Phases                    |

## Parallel Execution Opportunities

Tasks marked with `[P]` are candidates for parallel implementation. For example:
- **T012** (unit tests for `add_task`) and **T013** (unit tests for `get_all_tasks`) can be written in parallel to **T010** (implement `add_task`) and **T011** (implement `get_all_tasks`), assuming the method signatures are agreed upon.
- Test file creation tasks (**T005**, **T006**) can be done in parallel with directory creation.
- Unit tests can often be developed in parallel with the core logic functions they test, especially if the function signatures are stable.
- Integration tests can be developed once the core CLI interaction for a feature is stable.

## Implementation Strategy

The implementation will follow an iterative, MVP-first approach.

1.  **Phase 1 & 2 (Setup & Foundational)** will be completed first to establish the project environment and core data structures.
2.  **Phase 3 (User Story 1 - Add and View Tasks)** will form the Minimum Viable Product (MVP), allowing users to perform the most basic and essential functions of a todo application.
3.  Subsequent user story phases (4, 5, 6) will be implemented incrementally, building upon the MVP and each providing a new set of testable features.
4.  **Phase 7 (Polish & Cross-Cutting Concerns)** will address overall quality, robustness, and user experience improvements once all core functional requirements are met.

This strategy ensures continuous delivery of value and allows for early testing and feedback.

## Suggested MVP Scope

The suggested MVP scope includes all tasks within:
- **Phase 1: Setup**
- **Phase 2: Foundational Components**
- **Phase 3: User Story 1 - Add and View Tasks (P1)**

This MVP will provide a functional CLI application where users can add tasks and view their list.
