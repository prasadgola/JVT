// import {how} from 'javasript.js';
// //console.log(why);
// console.log(how(2,3));

//

// console.log(23)

// let info={
// 	name:"anil shidh",
// 	tellname:function()
// 	{
// 		return this.name;
// 	}
// }
// otherinfo= info.tellname;
// console.log(otherinfo.bind(info)());


// class Bindinfo{
// 	constructor()
// 	{
// 		this.name="anil shidhu";
// 		this.hello=this.hello.bind(this)
// 	}
// 	hello(){
// 		return this.name;
// 	}
// }info=new Bindinfo();
// otherinfo=info.hello;
// console.log(otherinfo())


class App{
	hello()
	{
		alert("hello");
	}
	render(){
		return(
			<div className="App">
			<button onClick={this.hello.bind(this)}>say easd</button>
			</div>
			);
	}
}