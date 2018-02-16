
var app = angular.module("favSongsApp", ["ngRoute"]);

app.service("favSongsServ", function () {
    var user = null;
    favSongs = this;

    this.setUser = function(user) {
        favSongs.user = user;
    }

    this.getUser = function() {
        return favSongs.user;
    }
});

app.config(function($routeProvider, $locationProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "/static/html/users.html",
        controller : "UsersCtrl"
    })
    .when("/users", {
        templateUrl : "/static/html/users.html",
        controller : "UsersCtrl"
    })
    .when("/songs", {
        templateUrl : "/static/html/songs.html",
        controller : "SongsCtrl"
    })

    $locationProvider.html5Mode(true);
});

app.controller("UsersCtrl", ["$scope", "$http", "$location", "favSongsServ", function ($scope, $http, $location, favSongsServ) {

    $scope.getUsers = function () {
        $http.get('api/users/').then(function (data, status, headers, config) {
            $scope.users = data.data;
        }, function (data, status, headers, config) {
            console.log("Error getting users")
        });
    }

    $scope.addUser = function() {
        $scope.newUserForm=false;

        var parameter = JSON.stringify({
            "name": $("#new-user-name").val(),
            "email": $("#new-user-email").val()
        });

        $http.post('api/users/', parameter).then(function (data, status, headers, config) {
            $scope.getUsers();
        }, function (data, status, headers, config) {
            console.log("Error saving user")
        });
    }

    $scope.deleteUser = function($event, userIndex) {
        $event.stopPropagation();

        $http.delete('api/users/' + $scope.users[userIndex].id + '/').then(function (data, status, headers, config) {
            $scope.getUsers();
        }, function (data, status, headers, config) {
            console.log("Error deleting user")
        });
    }

    $scope.goToSongsPage = function(user) {
        favSongsServ.setUser(user);
        $location.path("/songs");
    }

    $scope.newFavSongForm = false;
    $scope.getUsers();
}]);


app.controller("SongsCtrl", ["$scope", "$http", "$location", "favSongsServ", function ($scope, $http, $location, favSongsServ) {
     $scope.getAllSongs = function () {
        $http.get('api/songs/').then(function (data, status, headers, config) {
            $scope.songs = data.data;
        }, function (data, status, headers, config) {
            console.log("Error getting songs")
        });
    }

    $scope.getFavSongs = function() {
        $http.get('api/songs/user/' + $scope.user.id + '/').then(function (data, status, headers, config) {
            $scope.favSongs = data.data;
        }, function (data, status, headers, config) {
            console.log("Error getting songs")
        });
    }

    $scope.addFavoriteSong = function() {
        $scope.newFavSongForm = false;

        var newSongInfo = JSON.stringify({
            "command": "add",
            "song_id": $('#select-fav-song option:selected').attr('id')
        });

        $http.post('api/songs/user/' + $scope.user.id + '/', newSongInfo).then(function (data, status, headers, config) {
            $scope.getFavSongs();
        }, function (data, status, headers, config) {
            console.log("Error adding favorite song")
        });
    }

    $scope.deleteFavoriteSong = function(songIndex) {

        var songInfo = JSON.stringify({
            "command": "delete",
            "song_id": $scope.favSongs[songIndex].id
        });

        $http.post('api/songs/user/' + $scope.user.id + '/', songInfo).then(function (data, status, headers, config) {
            $scope.getFavSongs();
        }, function (data, status, headers, config) {
            console.log("Error deleting song")
        });
    }

    $scope.goBackToUsers = function(user) {
        $location.path("/users");
    }

    $scope.user = favSongsServ.getUser();
    $scope.getFavSongs();
}]);
