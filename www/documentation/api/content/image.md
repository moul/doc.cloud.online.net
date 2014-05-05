### group Images resources

This resources of API methods allows you to create, manage or delete your images.

#### Operation on a collection of images [/images]

##### Create a new image [POST]

+ Parameters
    + organization (required, string, `f030e920-9743-4f28-8164-964ba8555fa5`)... Organization unique identifier
    + name (required, string, `my_image`)... The image name
    + arch (required, string, `arm`)... The architecture type
    + root_volume (required, string, `8a8095d7-7db0-40c6-b867-0c0708f5e918`)... The root volume unique identifier

+ Request (application/json)

    + Body

            {
                "organization": "f030e920-9743-4f28-8164-964ba8555fa5",
                "arch": "arm",
                "name": "my_image",
                "root_volume": "8a8095d7-7db0-40c6-b867-0c0708f5e918"
            }

+ Response 201 (application/json)

        {
            
        }

+ Response 400

+ Response 401

+ Response 403

##### Retrieves the list all existing images [GET]

+ Response 200 (application/json)

        {
            "images": []   
        }

+ Response 401

+ Response 403

#### Operation on a single image [/images/{image_id}]

+ Parameters
    + image_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Image unique identifier

##### Retrieves informations about an image [GET]

+ Response 200 (application/json)

        {
            "images": {

            }
        }

+ Response 401

+ Response 403

+ Response 404

##### Update informations about an image [PUT]

+ Parameters
    + image_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Image unique identifier
    + TODO (required, string, `TODO`)... TODO

+ Request (application/json)

    + Body

            {
                TODO
            }


+ Response 200 (application/json)

        {
            "images": {
            
            }
        }

+ Response 401

+ Response 403

+ Response 404

##### Delete an image [DELETE]

+ Response 204

+ Response 403

+ Response 404

