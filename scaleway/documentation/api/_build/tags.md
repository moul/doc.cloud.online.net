

###group Tags
#resources related to scaleway Tags.
####List tags [/tags?limit&server_id&name]
Retrieves tags granted for user<br />Retrieves tags and associated metadatas
#####[GET]

+ Parameters
	+ limit (required, string)... Maximum number of objects, default value is 100
	+ server_id (required, string)... Filter tags attached to an server
	+ name (required, string)... Filter by tag name

####Tag info [/tags/{tag_id}]
Retrieves detailed info about a tag
#####[GET]

+ Parameters
	+ tag_id (required, string)... Tag unique identifier

####Add tag [/tags]
Creates and provisions a new tag
#####[POST]

+ Parameters

####Edit tag [/tags/{tag_id}]
Updates info of a tag
#####[PUT]

+ Parameters
	+ tag_id (required, string)... tag unique identifier

####Delete tag [/tags/{tag_id}]
Deletes and deprovisions a tag
#####[DELETE]

+ Parameters
	+ tag_id (required, string)... Tag unique identifier

####List tag metadata [/tags/{tag_id}/metadatas?limit]
Retrieves tags granted for user
#####[GET]

+ Parameters
	+ tag_id (required, string)... Container unique identifier
	+ limit (required, string)... Maximum number of objects, default value is 100
	+ key (required, string)... Filter by key

####Create tag metadata [/tags/{tag_id}/metadatas]
Creates metadata
#####[POST]

+ Parameters
	+ tag_id (required, string)... Container unique identifier
	+ metadata_key (required, string)... Metadata key
	+ metadata_value (required, string)... New metadata value

####Update tag metadata [/tags/{tag_id}/metadatas/{metadata_key}]
Updates info of a container
#####[PUT]

+ Parameters
	+ tag_id (required, string)... Container unique identifier
	+ metadata_key (required, string)... Metadata key
	+ metadata_value (required, string)... New metadata value

####Delete tag metadata [/tags/{tag_id}/metadatas/{metadata_key}]
Deletes and deprovisions a tag
#####[DELETE]

+ Parameters
	+ tag_id (required, string)... Tag unique identifier
	+ metadata_key (required, string)... Metadata key

