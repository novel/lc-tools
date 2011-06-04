var lctools = {
        numposts: 3,

	news: function(json) {
		for (var i = 0; i < lctools.numposts; i++) {
			var post = json.feed.entry[i];
			var postTitle = post.title.$t;
			var postContent = post.content.$t;
			var postPublished = Date.parse(post.published.$t.replace(/\.\d{3}([\-\+])/, "$1"));
			
			var prettyPostPublished = $.easydate.format_date(postPublished);
			var tags = '';
			var postLink;
			var j = 0;

			// fetch post link
			for (var k = 0; k < post.link.length; k++) {
				if (post.link[k].rel == 'alternate') {
					postLink = post.link[k].href;
					break;
				}
			}

			$("<li><a href='" + postLink + "'><h3>" + postTitle + " :: " + 
					prettyPostPublished + "</h3></a><div>" + 
					postContent + "</div></li>").appendTo("#news_list");
		}
	},

};
