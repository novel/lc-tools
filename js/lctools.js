var lctools = {
        numposts: 3,

	news: function(json) {
		for (var i = 0; i < lctools.numposts; i++) {
			var post = json.feed.entry[i];
			var postTitle = post.title.$t;
			var postContent = post.content.$t;
			var tags = '';
			var postLink;
			var j = 0;

			// create command-separated link of tags
			/*while (j < post.category.length - 1) {
				tags += post.category[j].term + ", ";
				j++;
			}
			tags += post.category[j].term;*/

			// fetch post link
			for (var k = 0; k < post.link.length; k++) {
				if (post.link[k].rel == 'alternate') {
					postLink = post.link[k].href;
					break;
				}
			}

			$("<li><a href='" + postLink + "'><h3>" + postTitle + "</h3></a><div>" + postContent + "</div></li>").appendTo("#news_list");
		}
	},

};
