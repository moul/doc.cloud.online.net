### group Images
Resources related to images

#### Images Collection [/images]
A collection of images with all their details

##### Create an image [POST]
Create a new image

+ Parameters

+ Request (application/json)

    + Body

            {
                
            }

+ Response 201 (application/json)

+ Response 400

+ Response 401

##### List all images [GET]
Retrieve a list of images with all their details

+ Response 200 (application/json)

        {
            
        }


#### Image [/images/{image_id}]
A single image with all its details

+ Parameters

    + image_id (required, string, `4e0b46e4-7c1d-44d4-8ba6-dc5f80694397`)... Image unique identifier

##### Retrieve an image [GET]
Retrieve details about a image

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Update details about an image [PUT]

+ Response 200 (application/json)

        {
        }

+ Response 404

##### Remove an image [DELETE]

+ Response 204

+ Response 404

