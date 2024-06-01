add_to_card_schema = {
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
            "added_art_ids": {
              "type": "array",
              "items": {
                "type": "integer"
              },
              "additionalItems": False
            },
            "failed_art_ids": {
              "type": "array",
              "items": {
                "items": {},
                "additionalItems": False,
                "additionalProperties": False
              },
              "additionalItems": False
            }
          },
          "additionalProperties": False,
          "required": [
            "added_art_ids",
            "failed_art_ids"
          ]
        }
      },
      "additionalProperties": False,
      "required": [
        "data"
      ]
    }
  },
  "additionalProperties": False,
  "required": [
    "status",
    "error",
    "payload"
  ]
}