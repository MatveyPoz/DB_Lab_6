# Проєктування бази даних
 
 
## Модель бізнес-об'єктів

```plantuml
@startuml

entity Permission #14f749
entity Permission.id
entity Permission.name
entity Permission.description
entity Permission.role_permission

Permission.id --* Permission
Permission.name --* Permission
Permission.description --* Permission
Permission.role_permission --* Permission 
 
entity Role #0c56bd
entity Role.id
entity Role.user_role
entity Role.description
entity Role.name

Role.id --* Role
Role.user_role --* Role
Role.description --* Role
Role.name --* Role
Permission.role_permission -u- Role

entity User #bd0c65
entity User.id
entity User.name
entity User.lastname
entity User.password

User.id --* User
User.name --* User
User.lastname --* User
User.password --* User
Role.user_role -u- User

entity Survey #e9d201
entity Survey.id
entity Servey.user_id
entity Survey.name
entity Survey.description
entity Servey.result

Survey.id --* Survey
Servey.user_id --* Survey
Survey.name --* Survey
Survey.description --* Survey
Servey.result --* Survey
User -r- Servey.user_id

entity Result #00ff61
entity Result.id
entity Result.description
entity Result.name

Result.id --* Result
Result.description --* Result
Result.name --* Result
Servey.result -u- Result

@enduml
``` 

## ER-модель
```plantuml
@startuml

entity Permission {
  +id: int
  +name: string
  +description: string
}

entity Role {
  +id: int
  +name: string
  +description: string
}

entity User {
  +id: int
  +name: string
  +lastname: string
  +password: string
}

entity Survey {
  +id: int
  +name: string
  +description: string
}

entity Question {
  +id: int
  +text: string
  +type: enum {open, closed, multiply_choice}
  +isNecessary: bool
}

entity Result {
  +id: int
  +name: string
  +description: string
}

entity AnswerOption {
  +id: int
  +text: string
}

entity UserAnswer {
  +id: int
  +answer: string
}

Permission -- "0..*" Role : assigns >
Role -- "0..*" User : contains >
Role -- "0..*" Permission : grants >

User -- "0..*" Survey : completes >
Survey -- "1..*" Question : answers
Survey -- "1..*" Result : generates >
Question -- "0..*" AnswerOption : has
Result -- "1..*" UserAnswer : contains
UserAnswer -- "1..*" Question : answers
Question -- "1..*" UserAnswer : isAnsweredIn


@enduml
```

##  Реляційна схема

![relational-schema](https://github.com/user-attachments/assets/cf55f090-77ab-4c5a-89e2-a522d5a49361)



