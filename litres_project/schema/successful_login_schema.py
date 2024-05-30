login = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "integer"
    },
    "error": {
      "type": "null"
    },
    "payload": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "sid": {
              "type": "string"
            }
          },
          "additionalProperties": True,
          "required": [
            "sid"
          ]
        }
      },
      "additionalProperties": True,
      "required": [
        "data"
      ]
    }
  },
  "additionalProperties": True,
  "required": [
    "status",
    "error",
    "payload"
  ]
}