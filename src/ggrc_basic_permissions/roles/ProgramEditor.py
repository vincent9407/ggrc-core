# Copyright (C) 2018 Google Inc.
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

scope = "Private Program"
description = """
  A user with authorization to edit mapping objects related to an access
  controlled program.<br/><br/>When a person has this role they can map and
  unmap objects to the Program and edit the Program info, but they are unable
  to delete the Program or assign other people roles for that program.
  """
permissions = {
    "read": [
        "Document",
        "ObjectObjective",
        "ObjectPerson",
        "Program",
        "Relationship",
        "UserRole",
        "Context",
    ],
    "create": [
        "Audit",
        "Snapshot",
        "Document",
        "ObjectObjective",
        "ObjectPerson",
        "Relationship",
    ],
    "view_object_page": [
        "__GGRC_ALL__"
    ],
    "update": [
        "Snapshot",
        "Document",
        "ObjectObjective",
        "ObjectPerson",
        "Program",
        "Relationship"
    ],
    "delete": [
        "Program",
        "Document",
        "ObjectObjective",
        "ObjectPerson",
        "Relationship",
    ]
}
