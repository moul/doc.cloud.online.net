

###group Volumes
#resources related to scaleway Volumes.
####List volumes [/volumes]
Lists volumes
#####[GET]

+ Parameters

####Create volume [/volumes]
Creates a new volume<br />This creates a volume. Volume is not attached by default.
#####[POST]

+ Parameters
	+ size (integer) (required, string)... the size of the volume to create
	+ base_volume (string) (required, string)... the id of the base volume
	+ base_snapshot (string) (required, string)... the id of the base snapshot
	+ type (string) (required, string)... the type of the volume

####Volume info [/volumes/{volume_id}]
Retrieves detailed info about a volume
#####[GET]

+ Parameters
	+ volume_id (required, string)... Volume unique identifier

