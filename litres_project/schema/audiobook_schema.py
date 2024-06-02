audiobook_schema = {
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
            "name": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "description": {
              "type": "null"
            },
            "content": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "title": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string",
                    "enum": [
                      "art_slider",
                      "collections_slider",
                      "genre_block",
                      "genre_slider"
                    ]
                  },
                  "content_url": {
                    "type": "string"
                  },
                  "linked_tab": {
                    "type": "null"
                  },
                  "webpage_url": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "content_type": {
                    "type": "null"
                  },
                  "faceted_content_url": {
                    "type": [
                      "string",
                      "null"
                    ]
                  },
                  "info_url": {
                    "type": "string"
                  },
                  "top_arts_url": {
                    "type": "string"
                  },
                  "required_params": {
                    "type": "object",
                    "properties": {
                      "art_types": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "enum": [
                            "audiobook"
                          ]
                        },
                        "additionalItems": False
                      }
                    },
                    "additionalProperties": False,
                    "required": [
                      "art_types"
                    ]
                  },
                  "webpage_url_params": {
                    "type": "object",
                    "properties": {
                      "art_types": {
                        "type": "array",
                        "items": {
                          "type": "string",
                          "enum": [
                            "audiobook"
                          ]
                        },
                        "additionalItems": False
                      }
                    },
                    "additionalProperties": False,
                    "required": [
                      "art_types"
                    ]
                  },
                  "additional_genres_url": {
                    "type": "string"
                  },
                  "content_covers_url": {
                    "type": "string",
                    "enum": [
                      "/api/genres/covers?art_types=audiobook"
                    ]
                  }
                },
                "additionalProperties": False,
                "required": [
                  "name",
                  "title",
                  "type",
                  "webpage_url"
                ]
              },
              "additionalItems": False
            }
          },
          "additionalProperties": False,
          "required": [
            "name",
            "title",
            "type",
            "description",
            "content"
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