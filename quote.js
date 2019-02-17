$w.onReady(function () {
	//TODO: write your page related code here...
	let quoteslist=["Try a new exercise with a friend","Enjoy a mean with no distractions","Put important numbers on your phone","Go on a friend date","Send someone an encouraging message","Take a movement break","Introduce a friend to your favourite book","Express yourself creatively","Spend some time outside","Try a new fruit or Vegetable","Dance to your favourite song"]
	$w('#quotes').text=quoteslist[parseInt(Math.random()*quoteslist.length)]
	 
});