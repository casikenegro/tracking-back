(window.webpackJsonp=window.webpackJsonp||[]).push([[6],{267:function(e,t,n){"use strict";n(60);var r=n(12),a=n(21),i=n(30),c=n(24),u=n(22),l=n(23),s=n(1),o=n.n(s),p=n(40);t.a=function(e){var t=function(t){function n(){return Object(a.a)(this,n),Object(c.a)(this,Object(u.a)(n).apply(this,arguments))}return Object(l.a)(n,t),Object(i.a)(n,[{key:"render",value:function(){var t=this.props.isSuperuser;return null===t?o.a.createElement(r.a,{type:"loading"}):t?o.a.createElement(e,this.props):o.a.createElement(o.a.Fragment,null)}}]),n}(s.Component);return Object(p.b)(function(e){return{isSuperuser:e.data_user.super_user}},null)(t)}},496:function(e,t,n){"use strict";n.r(t);var r=n(21),a=n(30),i=n(24),c=n(22),u=n(23),l=n(13),s=n(1),o=n.n(s),p=n(130),m=(n(79),n(31)),k=(n(61),n(25)),b=(n(99),n(37)),f=n(267),d=(b.a.Group,Object(f.a)(function(e){return o.a.createElement(p.c,null,o.a.createElement(p.e,null,"Configurar Tienda"),o.a.createElement(p.d,null,o.a.createElement(m.a,{onSubmit:e.setLink},o.a.createElement(b.a,{type:"url",id:"link-input",name:"link",placeholder:"Link",defaultValue:e.link}),o.a.createElement(p.k,{color:"muted"},"Asegurese de ingresar el link correspondiente"),o.a.createElement(k.a,{htmlType:"submit"},"Guardar"))))})),h=function(e){function t(){return Object(r.a)(this,t),Object(i.a)(this,Object(c.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(a.a)(t,[{key:"render",value:function(){return o.a.createElement("div",{className:"animated fadeIn"},o.a.createElement(p.s,{className:"justify-content-center"},o.a.createElement(p.f,{xs:"12",lg:"0"},o.a.createElement(d,{link:this.props.link,setLink:this.props.setLink}))))}}]),t}(s.Component),j=n(40),v=n(133),O=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(i.a)(this,Object(c.a)(t).call(this,e))).componentDidMount=function(){n.props.getLinkShopFromServer()},n.setLinkInServer=function(e){e.preventDefault();var t=document.getElementsByName("link")[0].value;t&&n.props.setLinkShopInServer(t)},n.setLinkInServer=n.setLinkInServer.bind(Object(l.a)(Object(l.a)(n))),n}return Object(u.a)(t,e),Object(a.a)(t,[{key:"render",value:function(){return o.a.createElement(h,{link:this.props.link,setLink:this.setLinkInServer})}}]),t}(s.Component),E={getLinkShopFromServer:v.b,setLinkShopInServer:v.e};t.default=Object(j.b)(function(e){return{link:e.link}},E)(O)}}]);
//# sourceMappingURL=6.1b883045.chunk.js.map