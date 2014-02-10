'use strict';

module.exports = function(grunt) {

	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		aglio: {
			api1:{
				files:{
					'documentation/api/index.html': [
						'documentation/api/content/api_general.md',
						'documentation/api/content/dns.md',
						'documentation/api/content/auth.md',
						'documentation/api/content/ticket.md',
		/*'documentation/api/_build/containers.md',*/
		/*'documentation/api/_build/organizations.md',*/
		/*'documentation/api/_build/servers.md',*/
		/*'documentation/api/_build/tags.md',*/
		/*'documentation/api/_build/volumes.md'*/
					]
				},
				theme: 'default',
				seperator: "\n"
			}
		},
		wintersmith: {
			build_docs_internal: {
				options: {
					config: 'config/wsconfig_docs_internal.json'
				}
			},
			build_docs: {
				options: {
					config: 'config/wsconfig_docs_public.json'
				}
			}
		}
	});
	grunt.loadNpmTasks('grunt-aglio');
	grunt.loadNpmTasks('grunt-wintersmith');

	grunt.registerTask('default', ['aglio', 'wintersmith']);
};
