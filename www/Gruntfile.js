'use strict';

module.exports = function(grunt) {

	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		clean: {
			dist: {
				files: [{
					dot: true,
					src: [
						'dist/*',
						'dist/.git*'
					]
				}]
			}
		},
		aglio: {
			api1:{
				files:{
					'dist/api/index.html': [
						'documentation/api/content/api_general.md',
		/*'documentation/api/content/dns.md',*/
						'documentation/api/content/account.md',
						'documentation/api/content/server.md',
						'documentation/api/content/volume.md',
						'documentation/api/content/snapshot.md',
						'documentation/api/content/image.md',
						// 'documentation/api/content/container.md',
						// 'documentation/api/content/ticket.md',
						'documentation/api/content/metadata.md',
		/*'documentation/api/_build/containers.md',*/
		/*'documentation/api/_build/organizations.md',*/
		/*'documentation/api/_build/servers.md',*/
		/*'documentation/api/_build/tags.md',*/
		/*'documentation/api/_build/volumes.md'*/
					]
				},
				theme: 'aglio/themes/flatly-multi.jade',
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
	/*grunt.loadNpmTasks('grunt-clean');*/
	/*grunt.loadNpmTasks('grunt-aglio');*/
	/*grunt.loadNpmTasks('grunt-wintersmith');*/
	require('load-grunt-tasks')(grunt);
	grunt.registerTask('default', ['clean', 'aglio', 'wintersmith']);
};
