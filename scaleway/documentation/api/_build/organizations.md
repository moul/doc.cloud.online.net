

###group Organizations
#resources related to scaleway Organizations.
####List organizations [/organizations]
Retrieves full details of all organizations.
#####[GET]

+ Parameters

####List a summary of organizations [/organizations/summary]
Retrieves a list of IDs, names and levels of all organizations.
#####[GET]

+ Parameters

####Add organization [/organizations]
Create a new organization.
#####[POST]

+ Parameters
	+ name (string) (required, string)... organization name
	+ address_line1 (string) (required, string)... 
	+ address_zip (string) (required, string)... 
	+ address_city (string) (required, string)... 
	+ address_country (string) (required, string)... 
	+ technical_contacts (required, string)... list of technical contacts ids
	+ administrative_contacts (required, string)... list of administrative contacts ids
	+ billing_contacts (required, string)... list of billing contacts ids
	+ address_line2 (string) (required, string)... 
	+ address_state (string) (required, string)... 

####Get organization [/organizations/{id}]
Get all information about an organization.
#####[GET]

+ Parameters
	+ id (UUID) (required, string)... Organization unique ID

####Edit/update organization [/organizations/{id}]
Edit/update an organization.
#####[PUT]

+ Parameters
	+ id (UUID) (required, string)... Organization unique ID
	+ name (string) (required, string)... organization name
	+ technical_contacts (required, string)... list of technical contacts ids
	+ administrative_contacts (required, string)... list of administrative contacts ids
	+ billing_contacts (required, string)... list of billing contacts ids
	+ address_line1 (string) (required, string)... 
	+ address_line2 (string) (required, string)... 
	+ address_zip (string) (required, string)... 
	+ address_state (string) (required, string)... 
	+ address_city (string) (required, string)... 
	+ address_country (string) (required, string)... 

####Delete organization [/organizations/{id}]
Delete an organization
#####[DELETE]

+ Parameters
	+ id (UUID) (required, string)... Organization unique ID

