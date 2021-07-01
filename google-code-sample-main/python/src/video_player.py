"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isPaused = False
        self.isPlaying = False
        self._current_video = None
        self._current_playlist = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        list_videos = self._video_library.get_all_videos()
        list_videos.sort(key=lambda x: x.title)
        print("Here's a list of all available videos: ")
        for video in list_videos:
            tagString = str(video.tags)
            print(f"{video.title} ({video.video_id}) [{tagString.strip}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot play video: Video does not exist")
            return
        if self._current_video != None:
            print(f"Stopping video: {self._current_video}")
            print(f"Playing video: {video.title}")
            self._current_video = video.title
            return

        print(f"Playing video: {video.title}")
        self._current_video = video.title

    def stop_video(self):
        """Stops the current video."""
        current_video = self._current_video
        if current_video != None:
            print(f"Stopping video:  {self._current_video}")
            self._current_video = None
        else:
            print("Cannot stop video: Video does not exist")
            self._current_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""

        getVideo = self._video_library.get_all_videos()
        numVideos = len(self._video_library.get_all_videos()) 

        if numVideos == 0:
            print("There are no videos available to play")
        else:
            if self.isPlaying is True:
                print("Stopping video:", self.currentVideo.title)
                self.isPaused = False
            pickVideo = random.choice(getVideo)
            print("Playing video:", pickVideo.title)
            self.isPlaying = True
            self.currentVideo = pickVideo

    def pause_video(self):
        """Pauses the current video."""

        current_video = self._current_video
        if self.isPaused == False:
            print(f"Pausing video:  {self._current_video}")
            self.isPaused = True
        else:
            print(f"Video already paused: {self._current_video}")

    def continue_video(self):
        """Resumes playing the current video."""
        current_video = self._current_video
        if current_video == None:
            print(f"Cannot continue video: No video is currently playing")
        else:
            if self.isPaused == True:
                print(f"Continuing video:  {self._current_video}")
                self.isPaused = False
            else:
                print(f"Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        current_video = self._current_video
        print(f"Currently playing: {self._current_video}")
        print("show_playing needs implementation")

##############################################################################

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self.playlist_name:
            print(f"Successfully created new playlist: {playlist_name}")
            self.playlists.append(playlist_name.lower())
            self._current_playlist = playlist_name
        else:
            print("Cannot create playlist: Playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        list_playlists = self._video_library.get_all_playlists()
        list_playlists.sort(key=lambda x: x.title)
        print("Showing all playlists: ")
        for playlist in list_playlists:  # Loop through txt file, reading each video line by line
            print(f"{playlist.name}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        playlist = self._video_library.get_playlist(playlist_name)

        if not playlist:
            print("Cannot play video: Video does not exist")
            return
        if self._current_video != None:
            print(f"Showing playlist: {self._current_video}")
            print(f"Playing video: {playlist.title}")
            self._current_video = playlist.title
            return

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

#########################################################################

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        list_videos = self._video_library.get_all_videos()
        list_videos.sort(key=lambda x: x.title)
        print(f"Here are the results for {search_term}: ")
        for video in list_videos:  # Loop through txt file, reading each video line by line
            if str(search_term) in video.title:
                print("###############")
                tagString = str(video.tags)  # Convert to string to allow stripping of brackets
                print(f"{video.title} ({video.video_id}) [{tagString.strip}]")

        #else:
             #   print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        list_videos = self._video_library.get_all_videos()
        list_videos.sort(key=lambda x: x.title)
        print(f"Here are the results for {video_tag}: ")
        for video in video_tag:  # Loop through txt file, reading each video line by line
            if str(video_tag) in video.tags:
                print("###############")
                tagString = str(video.tags)  # Convert to string to allow stripping of brackets
                print(f"{video.title} ({video.video_id}) [{tagString.strip}]")
        print("search_videos_tag needs implementation")

###########################################################################

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
