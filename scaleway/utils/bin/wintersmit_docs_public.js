var path = require('path');

// wintersmith module
var wintersmith = require('wintersmith');

// Configuration file for wintersmith
var wsconfig = wintersmith(path.join(__dirname, '../../config/wsconfig_docs_public.json'));

// Build the content tree and render it to outputDir.
wsconfig.build(function(error) {
  if (error) throw error;
  console.log('Done!');
});

// Start the preview server. Calls callback when server is up and running or if an error occurs.
wsconfig.preview(function(error, server) {
	if (error) throw error;
	console.log(server);
	console.log('Wintersmith server running!');
});


