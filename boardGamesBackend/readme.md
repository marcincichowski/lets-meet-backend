# Game controllers

## add_game <br>
  add games to database
 - path: /backend/game/add
 - based on POST
 - required from_body params: 
   - 'name': name of the game, string 
   - 'person_count': count of persons needed to play the game, int
   - 'is_online': True if added game is online or False if it's not, boolean
   - 'accepted_by_id': id of moderator who accept add game requests. int
   - 'requested_by_id' id of user who wants to add a game, int
   - 'description': descprition of the game, string
   - 'url': url for game in the store i.e. steam or qubz, string url
  - returns HttpResponse "ok" when game is succesfully added to database or returns exception if games wasn't added


## get_all_games <br>
 returns all games in database.
 - path: /backend/game/all
 - based on GET
 - returns all games from database.

## get_game_by_id <br>
 returns game based on given id.
 - path: /backend/game/get_id
 - based on GET,
 - required from_body params: 'id' = id of game
 - returns game record from database.

## update_game <br>
 in progresss

## delete_game <br>
 removes game from database.
 - path: /backend/game/delete
 - based on GET,
 - required from_body params: 'id' = id of game
 - returns HttpResponse when game is succesfully deleted from database or if game is not in database returns HttpResponse "Not found".

# User controllers

## add_user <br>
  add user to database
 - path: /backend/user/add
 - based on POST
 - required from_body params: 
   - 'username': name of the user, string 
   - 'email': email of the user, string
   - 'password': password of the user, string
  - returns HttpResponse "ok" when user is succesfully added to database or returns exception if user wasn't added

## get_all_users <br>
 returns all users in database.
 - path: /backend/user/all
 - based on GET
 - returns all users from database.

## get_user_by_id <br>
 returns user based on given id.
 - path: /backend/user/get_id
 - based on GET,
 - required from_body params: 'id' = id of user
 - returns user record from database.

## update_user <br>
 in progresss

## delete_user <br>
 removes user from database.
- path: /backend/user/delete
 - based on GET,
 - required from_body params: 'id' = id of user
 - returns HttpResponse when user is succesfully deleted from database or if user is not in database returns HttpResponse "Not found".

# Meeting controllers

## add_meeting <br>
  add meeting to database
add user to database
 - path: /backend/user/add
 - based on POST
 - required from_body params: 
   - 'is_online': True if meeting takes place online or not, boolean 
   - 'game_id': id of the game, int
   - 'owner_id': id of the meeting owner/host, int
  - returns HttpResponse "ok" when meeting is succesfully added to database or returns exception if meeting wasn't added

## get_all_meetings <br>
 returns all meetings in database.
 - path: /backend/meeting/all
 - based on GET
 - returns all meetings from database.

## get_meeting_by_id <br>
 returns meeting based on given id.
 - path: /backend/meeting/get_id
 - based on GET,
 - required from_body params:
   - 'id' = id of meeting, int
 - returns meeting record from database.

## update_meeting <br>
 in progresss

## delete_meeeting <br>
 removes meeting from database. 
 - path: /backend/meeting/delete
 - based on GET,
 - required from_body params: 
   - 'id' = id of meeting, int
 - returns HttpResponse 'deleted' when meeting is succesfully deleted from database or if meeting is not in database returns HttpResponse 'Not found'.


## add_user_to_meeting <br>
 add user to meeting based on user id and meeting id.
 - path: /backend/meeting/add_user
 - based on GET,
 - required from_body params: 
   - 'user_id' = id of user, int
   - 'meeting_id' = id of meeting, int 
 - returns HttpResponse 'Removed user from meeting' when user is succesfully removed from database or if meeting or user is not in database returns HttpResponse 'Not found'.


## remove_user_from_meeting <br>
 removes user from meeting based on user id and meeting id.
 - path: /backend/meeting/rm_user
 - based on GET,
 - required from_body params: 
   - 'user_id' = id of user, int
   - 'meeting_id' = id of meeting, int 
 - returns HttpResponse 'Added user to meeting ' when user is succesfully added to database or if meeting or user is not in database returns HttpResponse 'Not found'.


# other controllers <br>

## auth
 login user based on given credentials. 
 - path: /backend/authorize 
 - based on POST,
- required from_body params: 
   - 'username' = name of the user who wants to log in, string
   - 'password' = password of the user, string 
 - returns HttpResponse 'authorized' when user is succesfully logged in or HttpResponse 'Bad credentials' when not.

## logout
 ends session with logged user 

## index
 returns index.
- path: ''

## permission_denied
 returns HttpResponse "Not authorized"
- path: /backend/denied
