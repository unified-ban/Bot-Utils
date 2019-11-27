# Bot-Utils
Bot utilities, helpers and decorators

Here are all the functions of common use and tools in general.

This path contains 2 packages:
- decorators
- helpers

Tools such as the logger or daemon are present as files, while
decorators and helpers have their own subfolder.

## Examples
A set of functions for using the shell must be placed in the
Utils folder.

A single and recursive function to be used in a conditional
control must be inserted in the Utils, precisely in the helpers
subfolder if it is to be used within a function or in the
decorators folder if it is intended as an event or must be
performed before the main function.


## Files
### tools
* blacklist (synchronizer)
* daemon
* file (common operations)
* logger (custom exception logger)
* shell

### decorators
* bypass
* chat
* message
* permissions

### helpers
* h_chat
* h_group
* h_keyboard
* h_language
* h_message
* h_notes
* h_scam
* h_spam
* h_sql
* h_user
* h_variables
