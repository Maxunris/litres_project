invalid_login = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "title": {
          "type": "string"
        }
      },
      "additionalProperties": True,
      "required": [
        "type",
        "title"
      ]
    }
  },
  "additionalProperties": True,
  "required": [
    "status",
    "error"
  ]
}