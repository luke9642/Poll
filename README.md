# Poll app

## Overview
  
It's the Python Django application. Authenticated user can create new polls, manage and share them.
Anonymous user can fill and send the poll. Then authenticated user sees results individually and summary statistics.

## Structure

### Database:
  - SQLite database which keeps users, polls, questions and answers

### Models:
Python wrappers to `SQLite` database
  - __`choice`__ models: `RangeChoice`, `SingleChoice`, `TextChoice`, `TextareaChoice`
    - they keep value for questions types when user creates new poll
  - __`answer`__ models: `RangeAnswer`, `SingleAnswer`, `TextAnswer`, `TextareaAnswer`
    - they keep values of anonymous users` answers
  - __`question`__ model:
    - has `Poll` foregin key
    - base classes `Choice` and `Answer` have this model as foreign key
    - keeps `text`, `type` and `required` field
  - __`poll`__ model:
    - has references to questions and answers
    - has his own manager `PollManager` which inherts from Django `models.Manager`
    - fields are: `author`, `name`, `pub_date`
      
### Views and templates:
  - __`CreatePollView`__:
    - _get_: renders `form.html` template
    - _post_: creates new poll for authenticated user and returns JSON
  - __`PollsView`__:
    - inherits Django `ListView`
    - _get_: renders `polls.html` with list of user's polls
    - _delete_: removes poll with given poll hash and returns JSON
  - __`PollView`__:
    - expects `poll_hash`
    - _get_: renders `poll.html` for answering poll
    - _post_: renders `confirm.html` and adds new answer for poll
  - __`SummaryView`__:
    - _get_: renders `summary.html` with summary for all poll answers and draws graphs
  - __`AnswersView`__:
    - _get_: renders `answers.html` with each answer per page, pagination enabled
  - __`QuestionTypes`__:
    - _get_: returns JSON with question types available
  - __`UserRegisterView`__:
    - _get_: renders `register.html` with user registration form

### URLs:
 
| relative path   | view name         | path name       |
|-----------------|-------------------|-----------------|
| user/login/     | LoginView         | login           |
| user/register/  | UserRegisterView  | register        |
| user/logout/    | LogoutView        | logout          |
| polls/          | PollsView         | polls           |
| poll/new/       | CreatePollView    | poll_create     |
| confirm/        | TemplateView      | confirm         |
| question-types/ | QuestionTypes     | question-types  |

## Unit tests
  - written in _Django test_ which inherits Pythonic `unittest`
  - include testing poll creation, `PollController` usage, question types registry usage

## Other components
  - __`question_types_registry.Registry`__:
    - known for all components registry which keeps all choices and answers types
  - __`PollController`__:
    - controller for managing poll creation, deletion, new answers addition and fetching polls' data
  - __'to_json`__ filter:
    - allows mapping string to JSON object
