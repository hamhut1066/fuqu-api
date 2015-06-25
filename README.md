# fuqu-api

The FuQu API, responsible for data covering queue times for places.

# Install

To set up the project run `./.danger`. This will check you have the necessary dependencies and build the project, as well
as install git hooks to ensure all tests are ran before committing.

# Useful Commands

`./.serve` starts the API server running on localhost:8000 (linux) or 192.168.59.103:8000 (mac with boot2docker)  
`./.test` runs the entire test suite  
`./.test module.app.tests.TestClass.test_method` runs a more specific group of tests down to a specific test  
`./.migrate [app_name]` creates migrations for any changes to the data structure. Run this if modifying models.  
`./.manage [command]` runs a specified django management command  
