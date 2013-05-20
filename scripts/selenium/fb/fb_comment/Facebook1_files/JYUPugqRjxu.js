/*1364788801,178142531*/

if (self.CavalryLogger) { CavalryLogger.start_js(["QVJ60"]); }

__d("SubscriptionLevels",[],function(a,b,c,d,e,f){var g={ALL:'162318810514679',DEFAULT:'271670892858696',TOP:'266156873403755'};e.exports=g;});
__d("EditSubscriptions",["Event","function-extensions","Arbiter","AsyncRequest","CSS","DOM","ge","MenuDeprecated","Parent","SubscriptionLevels","arrayContains"],function(a,b,c,d,e,f){var g=b('Event');b('function-extensions');var h=b('Arbiter'),i=b('AsyncRequest'),j=b('CSS'),k=b('DOM'),l=b('ge'),m=b('MenuDeprecated'),n=b('Parent'),o=b('SubscriptionLevels'),p=b('arrayContains'),q=13,r=45,s=[o.ALL,o.DEFAULT,o.TOP],t={},u={},v={},w={},x={},y={},z={},aa={},ba={},ca={},da={},ea="/ajax/follow/follow_profile.php",fa="/ajax/follow/unfollow_profile.php",ga="/ajax/settings/notifications/notify_me.php",ha={},ia={},ja=null,ka=false;function la(ib){return p(s,ib);}function ma(ib,jb,kb,lb){var mb=n.byClass(lb,'uiMenuItem')||n.byClass(lb,'uiMenuXItem');if(!mb||!k.contains(ib,mb)){return;}else if(j.hasClass(mb,'SubscribeMenuSubscribeCheckbox')){if(v[jb]){pa(ib,jb);}else oa(ib,jb);return false;}else if(j.hasClass(mb,'SubscribeMenuUnsubscribe')){pa(ib,jb);return false;}else if(j.hasClass(mb,'SubscribeMenuSettingsItem')){cb(ib,true);return false;}else if(j.hasClass(mb,'SubscriptionMenuGoBack')){cb(ib,false);return false;}else if(j.hasClass(mb,'SubscriptionMenuItem')){na(ib,jb,kb,mb);return false;}else if(j.hasClass(mb,'SubscribeMenuNotifyMeCheckbox')){if(w[jb]){gb(ib,jb);}else fb(ib,jb);return false;}}function na(ib,jb,kb,lb){if(j.hasClass(lb,'SubscriptionMenuLevel')){if(m.isItemChecked(lb))return;ab(ib,jb,ta(lb),true,kb);}else if(j.hasClass(lb,'SubscriptionMenuCategory')){xa(jb,lb,!m.isItemChecked(lb),true,kb);}else if(j.hasClass(lb,'SubscriptionAppStory'))za(jb,lb,!m.isItemChecked(lb),kb);}function oa(ib,jb){var kb={profile_id:jb};h.inform('FollowingUser',kb);new i().setURI(ea).setMethod('POST').setData({profile_id:jb,location:qa(ib)}).setErrorHandler(h.inform.curry('FollowUserFail',kb)).send();}function pa(ib,jb){var kb={profile_id:jb};h.inform('UnfollowingUser',kb);new i().setURI(fa).setMethod('POST').setData({profile_id:jb,location:qa(ib)}).setErrorHandler(h.inform.curry('UnfollowUserFail',kb)).send();}function qa(ib){if(j.hasClass(ib,'followButtonFlyout')){return q;}else return r;}function ra(ib,jb,kb){var lb={profile_id:ib,level:aa[ib],custom_categories:ba[ib],location:kb};new i().setURI('/ajax/follow/manage_subscriptions.php').setData(lb).send();}function sa(ib,jb){var kb=ba[jb]||[],lb=m.getItems(ib);lb.forEach(function(mb){if(j.hasClass(mb,'SubscriptionMenuCategory')){var nb=ta(mb);if(p(kb,nb)){va(mb);}else wa(mb);}else if(j.hasClass(mb,'SubscriptionAppStory')){var ob=ta(mb);if(ia[jb]&&ia[jb][ob]){va(mb);}else wa(mb);}});ab(ib,jb,aa[jb],false);}function ta(ib){var jb=k.scry(ib,'input')[0];return jb&&jb.value;}function ua(ib){return k.find(ib,'a.itemAnchor');}function va(ib){j.addClass(ib,'checked');ua(ib).setAttribute('aria-checked',true);}function wa(ib){j.removeClass(ib,'checked');ua(ib).setAttribute('aria-checked',false);}function xa(ib,jb,kb,lb,mb){if(kb){va(jb);}else wa(jb);var nb=ta(jb);if(la(nb)){kb&&ya(ib,nb);}else if(kb){if(!p(ba[ib],nb))ba[ib].push(nb);}else{var ob=ba[ib].indexOf(nb);if(ob!==-1)ba[ib].splice(ob,1);}if(lb)ra(ib,nb,mb);}function ya(ib,jb){aa[ib]=jb;h.inform('SubscriptionLevelUpdated',{profile_id:ib,level:jb});}function za(ib,jb,kb,lb){var mb='/ajax/feed/filter_action/',nb=ta(jb),ob={actor_id:ib,app_id:nb};if(kb){va(jb);mb+='resubscribe_user_app/';ob.action='resubscribe_user_app';if(!ia[ib])ia[ib]={};ia[ib][nb]=true;}else{wa(jb);mb+='unsubscribe_user_app_checkbox/';ob.action='unsubscribe_user_app_checkbox';if(ia[ib])ia[ib][nb]=false;}new i().setURI(mb).setData(ob).send();}function ab(ib,jb,kb,lb,mb){var nb=k.scry(ib,'.SubscriptionMenuLevel'),ob=null;nb.forEach(function(pb){if(ta(pb)==kb){ob=pb;}else if(m.isItemChecked(pb))xa(jb,pb,false,false);});ob&&xa(jb,ob,true,lb,mb);}function bb(ib,jb,kb){v[jb]=kb;j.conditionClass(ib,'isUnsubscribed',!kb);var lb=k.scry(ib,'li.SubscribeMenuSubscribeCheckbox');if(lb.length!==0){var mb=lb[0];if(kb){va(mb);}else wa(mb);}}function cb(ib,jb){j.conditionClass(ib,'subscriptionMenuOpen',jb);}function db(ib,jb,kb){var lb=k.find(ib,".FriendListSubscriptionsMenu"),mb=k.find(lb,".uiMenuInner");if(ja!=null)ja.forEach(function(nb){mb.removeChild(nb);});kb.forEach(function(nb){mb.appendChild(nb);});ja=kb;}h.subscribe('UnfollowUser',function(ib,jb){if(ca[jb.profile_id]){ya(jb.profile_id,ca[jb.profile_id]);ba[jb.profile_id]=da[jb.profile_id].slice();}});h.subscribe('UpdateSubscriptionLevel',function(ib,jb){var kb=jb.profile_id+'',lb=jb.level+'';ya(kb,lb);var mb;for(mb in t)if(t[mb]===kb){var nb=l(mb);nb&&ab(nb,kb,lb,false);}});function eb(ib,jb,kb){w[jb]=kb;var lb=y[jb]&&!ka,mb=k.scry(ib,'li.SubscribeMenuNotifyMeCheckbox');if(mb.length!==0){var nb=mb[0];j.conditionShow(nb,!lb);j.conditionShow(k.find(ib,'li.SubscribeMenuNotifyMeCheckboxSeparator'),!lb);if(kb){va(nb);}else wa(nb);}}function fb(ib,jb){var kb={profile_id:jb};h.inform('EnableNotifsForUser',kb);new i().setURI(ga).setMethod('POST').setData({notifier_id:jb,enable:true}).setErrorHandler(h.inform.curry('EnableNotifsForUserFail',kb)).send();}function gb(ib,jb){var kb={profile_id:jb};h.inform('DisableNotifsForUser',kb);new i().setURI(ga).setMethod('POST').setData({notifier_id:jb,enable:false}).setErrorHandler(h.inform.curry('DisableNotifsForUserFail',kb)).send();}var hb={init:function(ib,jb,kb){var lb=k.getID(ib);if(!t[lb])g.listen(ib,'click',function(mb){return ma(ib,t[lb],kb,mb.getTarget());});if(kb===r&&ha[jb].length)db(ib,jb,ha[jb]);if(aa[jb])sa(ib,jb);t[lb]=jb;j.conditionClass(ib,'NonFriendSubscriptionMenu',!u[jb]);j.conditionClass(ib,'cannotSubscribe',!x[jb]);j.conditionClass(ib,'noSubscriptionLevels',y[jb]&&!z[jb]);j.conditionClass(ib,'noSubscribeCheckbox',!u[jb]&&!y[jb]);bb(ib,jb,v[jb]);eb(ib,jb,w[jb]);h.subscribe(['FollowUser','FollowingUser','UnfollowUserFail'],function(mb,nb){bb(ib,jb,true);}.bind(this));h.subscribe(['UnfollowUser','UnfollowingUser','FollowUserFail'],function(mb,nb){h.inform('SubMenu/Reset');bb(ib,jb,false);}.bind(this));h.subscribe(['EnableNotifsForUser','DisableNotifsForUserFail'],function(mb,nb){eb(ib,jb,true);}.bind(this));h.subscribe(['DisableNotifsForUser','EnableNotifsForUserFail'],function(mb,nb){eb(ib,jb,false);}.bind(this));h.subscribe('listeditor/friend_lists_changed',function(mb,nb){if(nb.notify_state){var ob=nb.added_uid?nb.added_uid:nb.removed_uid;eb(ib,ob,nb.notify_state.is_notified);}}.bind(this));cb(ib,false);},getSubscriptions:function(ib){return {level:aa[ib],custom_categories:ba[ib]};},setSubscriptions:function(ib,jb,kb,lb,mb,nb,ob,pb,qb,rb,sb,tb,ub){ya(ib,ob+'');u[ib]=jb;v[ib]=kb;x[ib]=lb;y[ib]=mb;z[ib]=nb;ca[ib]=qb+'';ba[ib]=pb.map(String);da[ib]=rb.map(String);ha[ib]=ub;w[ib]=sb;ka=tb;}};e.exports=a.EditSubscriptions||hb;});
__d("legacy:EditSubscriptions",["SubscriptionLevels","EditSubscriptions"],function(a,b,c,d){a.SubscriptionLevels=b('SubscriptionLevels');a.EditSubscriptions=b('EditSubscriptions');},3);
__d("DynamicFriendListEducation",["Event","Arbiter","AsyncRequest","Dialog","PageTransitions","arrayContains","createArrayFrom","removeFromArray"],function(a,b,c,d,e,f){var g=b('Event'),h=b('Arbiter'),i=b('AsyncRequest'),j=b('Dialog'),k=b('PageTransitions'),l=b('arrayContains'),m=b('createArrayFrom'),n=b('removeFromArray'),o,p,q,r,s,t;function u(){q&&q.hide();r&&r.hide();}function v(y){n(p,y);u();s({accept_tag_education:true});}function w(){u();s({nux_cancel:true});}var x={init:function(y,z){o=y;p=m(z).map(String);k.registerHandler(function(){u();o=false;s=undefined;p=[];});},showDialog:function(y,z,aa){if(o&&l(p,y)){u();h.inform('DynamicFriendListEducation/dialogOpen',{uid:z,flid:y});s=aa;q=new j().setAsync(new i('/ajax/friends/lists/smart_list_education.php').setMethod('GET').setData({flid:y,uid:z}).setReadOnly(true)).setHandler(v.bind(this,y)).setCloseHandler(function(){h.inform('DynamicFriendListEducation/dialogClosed',{uid:z,flid:y});}).setCancelHandler(function(){h.inform('DynamicFriendListEducation/dialogCancel',{uid:z,flid:y});}).show();}else aa();},showContextualDialog:function(y,z,aa,ba){if(o&&l(p,y)){u();t=aa;s=ba;new i('/ajax/friends/lists/smart_list_contextual_education.php').setMethod('GET').setData({flid:y,uid:z}).setReadOnly(true).send();}else ba();},setContextualDialog:function(y,z,aa,ba){r=y;r.setContext(t);r.show();g.listen(z,'click',v.bind(this,ba));g.listen(aa,'click',w);}};e.exports=x;});
__d("FriendStatus",["function-extensions","Arbiter","AsyncRequest","arrayContains","copyProperties","createArrayFrom"],function(a,b,c,d,e,f){b('function-extensions');var g=b('Arbiter'),h=b('AsyncRequest'),i=b('arrayContains'),j=b('copyProperties'),k=b('createArrayFrom');function l(p,q,r){this.id=p;this.update(q,r);}j(l.prototype,{update:function(p,q){p&&(this.status=p);if(q){this.lists=k(q).map(String);this._informListChange();}},isComplete:function(){return !!this.lists;},addToList:function(p){if(this.lists&&!i(this.lists,p))this.lists.push(p);this._informListChange();},removeFromList:function(p){if(this.lists){var q=this.lists.indexOf(p);q!==-1&&this.lists.splice(q,1);}this._informListChange();},updateList:function(p,q){q?this.addToList(p):this.removeFromList(p);},_informListChange:function(){g.inform('FriendListMembershipChange',{uid:this.id,lists:this.lists});}});j(l,{ARE_FRIENDS:1,INCOMING_REQUEST:2,OUTGOING_REQUEST:3,CAN_REQUEST:4});var m={},n={};function o(p,q,r){if(!m[r.uid]){m[r.uid]=new l(r.uid,p);}else m[r.uid].update(p);g.inform('FriendRequest/change',{uid:r.uid,status:p});}g.subscribe(['FriendRequest/cancel','FriendRequest/unfriend','FriendRequest/sendFail'],o.curry(l.CAN_REQUEST));g.subscribe(['FriendRequest/confirmFail'],o.curry(l.INCOMING_REQUEST));g.subscribe(['FriendRequest/cancelFail','FriendRequest/sent','FriendRequest/sending'],o.curry(l.OUTGOING_REQUEST));g.subscribe(['FriendRequest/confirm','FriendRequest/confirming'],o.curry(l.ARE_FRIENDS));j(l,{CLOSE_FRIENDS:null,ACQUAINTANCES:null,getFriend:function(p,q){if(m[p]&&m[p].isComplete()){q(m[p]);}else if(n[p]){n[p].push(q);}else{n[p]=[q];new h().setURI("/ajax/friends/status.php").setData({friend:p}).setHandler(function(r){var s=r.getPayload();l.initFriend.bind(l,p,s.status,s.lists).defer();}).send();}},initFriend:function(p,q,r){var s=m[p]||new l(p);s.update(s.status||q,s.lists||r);m[p]=s;n[p]&&n[p].forEach(function(t){t(s);});n[p]=null;},setSpecialLists:function(p){l.CLOSE_FRIENDS=p.close+'';l.ACQUAINTANCES=p.acq+'';}});e.exports=l;});
__d("FriendEditLists",["Arbiter","AsyncRequest","CSS","DOMQuery","DynamicFriendListEducation","EditSubscriptions","FriendStatus","MenuDeprecated","Parent","ScrollableArea","URI","$","arrayContains","copyProperties","ge"],function(a,b,c,d,e,f){var g=b('Arbiter'),h=b('AsyncRequest'),i=b('CSS'),j=b('DOMQuery'),k=b('DynamicFriendListEducation'),l=b('EditSubscriptions'),m=b('FriendStatus'),n=b('MenuDeprecated'),o=b('Parent'),p=b('ScrollableArea'),q=b('URI'),r=b('$'),s=b('arrayContains'),t=b('copyProperties'),u=b('ge'),v=5,w={},x='/ajax/profile/removefriendconfirm.php',y='/ajax/friends/requests/cancel.php',z='/ajax/choose/',aa='/profile.php',ba,ca;function da(oa,pa,qa){var ra=w[oa.id],sa=function(ta){var ua={action:qa?'add_list':'del_list',to_friend:ra.id,friendlists:[pa],source:ba};if(ta)t(ua,ta);ra.updateList(pa,qa);var va;if(qa&&pa==m.CLOSE_FRIENDS){va=ga(oa,m.ACQUAINTANCES);if(n.isItemChecked(va)){n.toggleItem(va);da(oa,m.ACQUAINTANCES,false);}}else if(qa&&pa==m.ACQUAINTANCES){va=ga(oa,m.CLOSE_FRIENDS);if(n.isItemChecked(va)){n.toggleItem(va);da(oa,m.CLOSE_FRIENDS,false);}}var wa={flid:pa,uid:ra.id},xa=qa?'FriendListHovercard/add':'FriendListHovercard/remove';g.inform(xa,wa);new h().setURI('/ajax/add_friend/action.php').setData(ua).send();};if(qa){k.showDialog(pa,ra.id,sa);}else sa();}function ea(oa){var pa=j.scry(oa,'input')[0];return pa&&pa.value;}function fa(oa,pa,qa){var ra={uid:pa.id};new h().setURI(y).setMethod('POST').setData({friend:pa.id}).setHandler(g.inform.bind(g,'FriendRequest/cancel',ra)).setErrorHandler(g.inform.bind(g,'FriendRequest/cancelFail',ra)).setStatusElement(qa).send();}function ga(oa,pa){var qa=n.getItems(oa);for(var ra=0;ra<qa.length;ra++)if(ea(qa[ra])==pa)return qa[ra];return null;}function ha(oa,pa){var qa=n.getItems(oa);qa.forEach(function(ra){var sa=ea(ra),ta=s(pa.lists,sa);if(n.isItemChecked(ra)!==ta)n.toggleItem(ra);});}function ia(oa){var pa=n.getItems(oa),qa=!i.hasClass(oa,'followButtonFlyout')&&!i.hasClass(oa,'likeButtonFlyout'),ra=[],sa=[],ta=0,ua=0;pa.forEach(function(za){if(i.hasClass(za,'neverHide')){i.removeClass(za,'underShowMore');ta++;}else if(n.isItemChecked(za)){ra.push(za);}else if(i.hasClass(za,'neverShow')||i.hasClass(za,'FriendListCreateTrigger')||(!qa&&i.hasClass(za,'friendOptionsOnly'))){i.addClass(za,'underShowMore');ua++;}else sa.push(za);});var va=v-ta,wa=ra.concat(sa),xa=ua;wa.forEach(function(za){if(i.hasClass(za,'ShowMoreItem')){va--;return;}if(va){i.removeClass(za,'underShowMore');va--;}else{i.addClass(za,'underShowMore');xa=true;}});i.conditionClass(oa,'hasMoreFriendListItems',xa);var ya=j.scry(oa,'.FriendListMenuShowMore');ya.forEach(function(za){i.removeClass(za,'FriendListMenuShowMore');});}function ja(oa,pa){i.conditionClass(oa,'FriendListMemorializedUser',pa);}function ka(oa,pa){i.conditionClass(oa,'FriendListCannotSuggestFriends',!pa);}function la(oa,pa){var qa=j.scry(oa,'.FriendListUnfriend')[0],ra=j.scry(oa,'.FriendListCancel')[0],sa=j.scry(oa,'.FriendListSuggestFriends')[0],ta=j.scry(oa,'.FriendListFriendship')[0];if(ra)i.conditionShow(ra,pa.status==m.OUTGOING_REQUEST);if(qa){i.conditionShow(qa,pa.status==m.ARE_FRIENDS);j.find(qa,'a').setAttribute('ajaxify',q(x).addQueryData({uid:pa.id,norefresh:true,unref:ca}).toString());}else i.conditionClass(oa,'NoFriendListActionSeparator',!ra||pa.status!=m.OUTGOING_REQUEST);if(sa)j.find(sa,'a').setAttribute('href',q(z).addQueryData({type:'suggest_friends',newcomer:pa.id,ref:'profile_others_dropdown'}).toString());if(ta){i.conditionShow(ta,pa.status==m.ARE_FRIENDS);j.find(ta,'a').setAttribute('href',q(aa).addQueryData({and:pa.id}).toString());}}function ma(oa,pa){var qa=j.scry(oa,'div.FriendListSubscriptionsMenu');if(qa.length!==0)l.init(oa,pa,45);}g.subscribe('FriendRequest/change',function(oa,pa){for(var qa in w){var ra=u(qa),sa=w[qa];if(ra&&sa&&sa.id==pa.uid){ha(ra,sa);la(ra,sa);ia(ra);}}});n.subscribe('select',function(oa,pa){if(i.hasClass(pa.item,'ShowMoreItem')&&i.hasClass(pa.menu,'FriendListMenu')){i.addClass(pa.menu,'FriendListMenuShowMore');p.poke(pa.item);}});var na={init:function(oa,pa,qa,ra,sa,ta){oa=r(oa);ba=qa;ca=ta;if(!w[oa.id])n.subscribe('select',function(ua,va){if(j.contains(oa,va.item))if(o.byClass(va.item,'FriendListItem')){n.toggleItem(va.item);var wa=ea(va.item);da(oa,wa,n.isItemChecked(va.item));}else if(o.byClass(va.item,'FriendListCancel')){fa(oa,w[oa.id],va.item);}else if(o.byClass(va.item,'FriendListUnfriend'))g.inform('FriendEditLists/unfriend');});i.addClass(oa,'async_saving');m.getFriend(pa,function(ua){ja(oa,ra);ka(oa,sa);ha(oa,ua);la(oa,ua);w[oa.id]=ua;ia(oa);ma(oa,pa);i.removeClass(oa,'async_saving');}.bind(this));}};e.exports=a.FriendEditLists||na;});
__d("FriendListFlyoutController",["Event","Arbiter","AsyncRequest","Button","ContextualLayer","CSS","DataStore","Dialog","DOM","DOMQuery","FriendEditLists","FriendStatus","Keys","Layer","LayerHideOnEscape","LayerTabIsolation","MenuDeprecated","Parent","ScrollableArea","Style","TabbableElements","UserAgent","emptyFunction"],function(a,b,c,d,e,f){var g=b('Event'),h=b('Arbiter'),i=b('AsyncRequest'),j=b('Button'),k=b('ContextualLayer'),l=b('CSS'),m=b('DataStore'),n=b('Dialog'),o=b('DOM'),p=b('DOMQuery'),q=b('FriendEditLists'),r=b('FriendStatus'),s=b('Keys'),t=b('Layer'),u=b('LayerHideOnEscape'),v=b('LayerTabIsolation'),w=b('MenuDeprecated'),x=b('Parent'),y=b('ScrollableArea'),z=b('Style'),aa=b('TabbableElements'),ba=b('UserAgent'),ca=b('emptyFunction'),da,ea,fa=null,ga=null,ha,ia,ja,ka,la,ma,na=1500,oa={init:function(ob){oa.init=ca;da=ob;da.subscribe('mouseenter',xa);da.subscribe('mouseleave',jb);da.subscribe('hide',ya);da.enableBehavior(v);da.enableBehavior(u);if(fa)o.setContent(da.getContent(),[fa,ga]);var pb=function(qb){var rb=x.byClass(qb.getTarget(),'enableFriendListFlyout');if(rb)if(ha===rb){clearTimeout(ka);}else{ea&&lb();ib(rb);}};g.listen(document.documentElement,{mouseover:pb,click:pb,keydown:function(event){var qb=event.getTarget();if(event.getModifiers().any)return;if(!ea||p.isNodeOfType(qb,['input','textarea']))return;var rb=g.getKeyCode(event),sb;switch(rb){case s.UP:case s.DOWN:var tb=wa();sb=ua(tb);sa(tb[sb+(rb===s.UP?-1:1)]);return false;case s.SPACE:var ub=ta(qb);if(ub){pa(ub);event.prevent();}break;default:var vb=String.fromCharCode(rb).toLowerCase(),wb=wa();sb=ua(wb);var xb=sb,yb=wb.length;while((~sb&&(xb=++xb%yb)!==sb)||(!~sb&&++xb<yb)){var zb=w.getItemLabel(wb[xb]);if(zb&&zb.charAt(0).toLowerCase()===vb){sa(wb[xb]);return false;}}}}});h.subscribe('FriendEditLists/unfriend',lb);h.subscribe('DynamicFriendListEducation/dialogOpen',function(){ma=true;});h.subscribe('DynamicFriendListEducation/dialogClosed',function(){ma=false;jb();});},initContent:function(ob){o.appendContent(document.body,ob);za(ob);(function(){if(!fa){fa=ob;da&&o.setContent(da.getContent(),[fa,ga]);l.show(fa);g.listen(fa,'click',mb);ea&&fb(ha);}else{o.remove(ob);ob=null;}}).defer();},initNux:function(ob){if(ga)return;ga=ob;da&&o.setContent(da.getContent(),[fa,ga]);},show:function(ob){gb(ob);},hide:function(ob){ob===false?lb():jb();},setActiveNode:function(ob){ea&&lb();ha=ob;ia=g.listen(ob,'mouseleave',function(){ha=null;ia&&ia.remove();});},setCloseListener:function(ob,pb){m.set(ob,'flfcloselistener',pb);if(ha!=ob)m.set(ob,'flfcloselistenertimeout',nb.curry(ob).defer(na));},setCloseListenerTimeout:function(ob){na=ob;}};function pa(ob){ba.firefox()&&ra(ob).blur();w.inform('select',{menu:qa(ob),item:ob});}function qa(ob){if(l.hasClass(ob,'uiMenuContainer'))return ob;return x.byClass(ob,'uiMenu');}function ra(ob){return p.find(ob,'a.itemAnchor');}function sa(ob){if(ob&&va(ob)){w._removeSelected(da.getContent());l.addClass(ob,'selected');ra(ob).focus();}}function ta(ob){return x.byClass(ob,'uiMenuItem');}function ua(ob){if(document.activeElement){var pb=ta(document.activeElement);return ob.indexOf(pb);}return -1;}function va(ob){return !l.hasClass(ob,'disabled')&&z.get(ob,'display')!=='none'&&z.get(x.byClass(ob,'uiMenu'),'display')!=='none';}function wa(){return w.getItems(da.getContent()).filter(va);}function xa(){clearTimeout(ka);}function ya(){if(ha){l.removeClass(ha,'selected');l.removeClass(ha,'uiButtonHover');if(m.get(ha,'flfcloselistener')){var ob=ha;m.set(ha,'flfcloselistenertimeout',nb.curry(ob).defer(na));}}ea=false;eb();ha=null;}function za(ob){var pb=p.scry(ob,'[tabindex="0"]');pb.forEach(function(qb){qb.tabIndex='-1';});pb[0]&&(pb[0].tabIndex='0');}function ab(ob){if(p.isNodeOfType(ob,'label')&&l.hasClass(ob,'uiButton'))ob=j.getInputElement(ob);return ob;}function bb(ob){return m.get(ab(ob),'profileid');}function cb(ob){return m.get(ab(ob),'memorialized')==='true';}function db(ob){return m.get(ab(ob),'cansuggestfriends')==='true';}function eb(){ia&&ia.remove();ia=null;la&&t.unsubscribe(la);la=null;ka&&clearTimeout(ka);ka=null;}function fb(ob){var pb=bb(ob),qb=cb(ob),rb=db(ob),sb=m.get(ob,'flloc'),tb=m.get(ob,'unref');q.init(fa,pb,sb,qb,rb,tb);l.conditionClass(fa,'followButtonFlyout',l.hasClass(ob,'profileFollowButton'));l.conditionClass(fa,'friendButtonFlyout',l.hasClass(ob,'FriendRequestFriends')||l.hasClass(ob,'FriendRequestIncoming')||l.hasClass(ob,'FriendRequestOutgoing'));l.conditionClass(fa,'likeButtonFlyout',l.hasClass(ob,'profileLikeButton'));var ub=p.scry(fa,'div.uiScrollableArea')[0];ub&&y.poke(ub);var vb=aa.find(fa)[0];vb&&vb.focus();}function gb(ob){if(!da||ea)return;da.setContext(ob);da.setCausalElement(ob);ob.setAttribute('aria-expanded','true');l.addClass(ob,'selected');l.addClass(ob,'uiButtonHover');da.show();ha=ob;ea=true;if(fa){fb(ob);}else new i().setURI('/ajax/friends/lists/flyout_content.php').setStatusElement(da.getContent()).send();eb();ia=g.listen(ob,'mouseleave',jb);la=t.subscribe('show',hb);if(m.get(ob,'flfcloselistener'))clearTimeout(m.remove(ob,'flfcloselistenertimeout'));var pb=bb(ob);r.getFriend(pb,function(qb){if(!ga)return;if(qb.status==r.OUTGOING_REQUEST){l.show(ga);i.bootstrap('/ajax/friends/lists/nux_flyout.php',null,true);}else l.hide(ga);});}function hb(ob,pb){if(!(pb instanceof k)||!p.contains(ha,pb.getContext()))jb();}function ib(ob){ha=ob;ja=gb.curry(ob).defer(350);ia=g.listen(ob,'mouseleave',function(){clearTimeout(ja);ha=null;ia&&ia.remove();});}function jb(){ka=lb.defer(150);}function kb(){var ob=n.getCurrent(),pb=ob&&ob.getBody();return !!(pb&&p.scry(pb,'.friendListDialogTourCarousel')[0]);}function lb(){if(ma||kb())return;ba.ie()<8&&document.documentElement.focus();if(da){da.hide();var ob=da.getCausalElement();ob&&ob.setAttribute('aria-expanded','false');}}function mb(event){var ob=x.byTag(event.getTarget(),'a');if(ob&&l.hasClass(ob,'FriendListActionItem'))jb();}function nb(ob){var pb=m.remove(ob,'flfcloselistener');pb&&pb();}e.exports=a.FriendListFlyoutController||oa;});
__d("SubscriptionFlyoutController",["Arbiter","CSS","DataStore","EditSubscriptions","Hovercard","HoverFlyout","$","emptyFunction"],function(a,b,c,d,e,f){var g=b('Arbiter'),h=b('CSS'),i=b('DataStore'),j=b('EditSubscriptions'),k=b('Hovercard'),l=b('HoverFlyout'),m=b('$'),n=b('emptyFunction'),o=null,p,q,r;function s(){var w=j.getSubscriptions(r);if(w){var x=w.custom_categories;if(x&&x.length===0)g.inform('UnfollowUser',{profile_id:r,from_hide_flyout:true});}}function t(w,x){r=i.get(x,'profile_id');var y=i.get(x,'loc');j.init(q,r,y);h.addClass(x,'selected');h.addClass(x,'uiButtonHover');if(i.get(x,'onclose'))clearTimeout(i.remove(x,'onclosetimeout'));}function u(w,x){r=null;h.removeClass(x,'selected');h.removeClass(x,'uiButtonHover');if(i.get(x,'onclose'))i.set(x,'onclosetimeout',function(){var y=i.remove(x,'onclose');y&&y();}.defer(1500));}var v={init:function(w,x){v.init=n;p=w;q=m(x);o=new l();o.init(w);o.setShowDelay(100).setHideDelay(150);o.subscribe('show',t);o.subscribe('hide',u);g.subscribe(['UnfollowUser','UnfollowingUser'],function(y,z){if(!z.from_hide_flyout&&z.profile_id==r){if(k.contains&&p)if(k.contains(p.getContext()))k.hide();o.hideFlyout(true);}});},initNode:function(w,x,y){i.set(w,'profile_id',x);i.set(w,'loc',y);o.initNode(w);},setActiveNode:function(w){o.setActiveNode(w);},show:function(w){o.showFlyout(w,true);},setCloseListener:function(w,x){if(o.getActiveNode()!==w){x();}else i.set(w,'onclose',x);}};e.exports=a.SubscriptionFlyoutController||v;});
__d("FollowButton",["Event","Arbiter","AsyncRequest","Button","CSS","DOM","FriendListFlyoutController","SubscriptionFlyoutController","SubscriptionLevels","URI","copyProperties"],function(a,b,c,d,e,f){var g=b('Event'),h=b('Arbiter'),i=b('AsyncRequest'),j=b('Button'),k=b('CSS'),l=b('DOM'),m=b('FriendListFlyoutController'),n=b('SubscriptionFlyoutController'),o=b('SubscriptionLevels'),p=b('URI'),q=b('copyProperties'),r=14;function s(w,x,y){k.conditionShow(x,y);k.conditionShow(w,!y);}function t(w,x){if(x&&k.hasClass(w,'enableFriendListFlyout')){m.show(w);}else m.hide();}function u(w,x,y){var z=l.scry(w,'.lowIcon')[0],aa=l.scry(w,'.medIcon')[0],ba=l.scry(w,'.highIcon')[0];if(!z||!aa||!ba)return;h.subscribe('SubscriptionLevelUpdated',function(ca,da){if(y===da.profile_id)switch(da.level){case o.ALL:j.setIcon(x,ba);break;case o.DEFAULT:j.setIcon(x,aa);break;case o.TOP:j.setIcon(x,z);break;}});}function v(w,x,y,z,aa,ba){this.init(w,x,y,z,aa,ba);}q(v.prototype,{init:function(w,x,y,z,aa,ba){if(!k.hasClass(y,'enableFriendListFlyout'))n.initNode(y,z,aa);if(aa==r&&k.shown(y))n.show(y);g.listen(x,'click',function(){s(x,y,true);n.setActiveNode(y);var ea=new p(x.getAttribute('ajaxify')),fa={profile_id:z,location:aa,source:'follow-button',subscribed_button_id:y.id,xids:ea.getQueryData().xids};new i().setURI(ba).setData(fa).setRelativeTo(y).send();});w&&u(w,y,z);h.subscribe(['FollowUser','FollowingUser','UnfollowUser','UnfollowingUser'],function(ea,fa){if(fa.profile_id==z)s(x,y,ea=='FollowUser'||ea=='FollowingUser');t(y,ea=='FollowUser');});var ca=false;h.subscribe('UnfollowingUser',function(ea,fa){if(fa.profile_id==z){ca=k.shown(y);ca&&s(x,y,false);}});h.subscribe('UnfollowUserFail',function(ea,fa){if(fa.profile_id==z&&ca)s(x,y,true);});h.subscribe('FollowUserFail',function(ea,fa){if(fa.profile_id==z&&ca)s(x,y,false);});var da=false;h.subscribe(['FriendRequest/sending','FriendRequest/confirming'],function(ea,fa){if(fa.uid==z){da=k.shown(x);da&&s(x,y,true);}});h.subscribe(['FriendRequest/sendFail','FriendRequest/confirmFail'],function(ea,fa){if(fa.uid==z&&da)s(x,y,false);});h.subscribe('FriendRequest/unfriend',function(ea,fa){(fa.uid==z)&&s(x,y,false);});}});e.exports=a.FollowButton||v;});
__d("AddFriendButton",["Event","Animation","Arbiter","AsyncRequest","AsyncResponse","collectDataAttributes","CSS","DOMQuery","FriendListFlyoutController","FriendStatus","ge","goURI","Style","URI"],function(a,b,c,d,e,f){var g=b('Event'),h=b('Animation'),i=b('Arbiter'),j=b('AsyncRequest'),k=b('AsyncResponse'),l=b('collectDataAttributes'),m=b('CSS'),n=b('DOMQuery'),o=b('FriendListFlyoutController'),p=b('FriendStatus'),q=b('ge'),r=b('goURI'),s=b('Style'),t=b('URI'),u={ERROR_ALREADY_ADDED:1431005,init:function(v,w,x,y,z,aa,ba,ca,da,ea,fa){var ga=v.id,ha=null,ia=n.scry(v,'.addButton')[0],ja=n.scry(v,'.addFriendText')[0],ka=n.scry(v,'.outgoingButton')[0],la=n.scry(v,'.incomingButton')[0],ma=n.scry(v,'.friendButton')[0];function na(ta,ua,va){var wa=new t(ia.getAttribute('ajaxify')),xa=l(v,['ft','gt']);new j().setURI(aa).setData({to_friend:w,action:ta,how_found:y,ref_param:z,link_data:xa,outgoing_id:ka.id,xids:wa.getQueryData().xids,logging_location:ba,no_flyout_on_click:ca,ego_log_data:da,http_referer:fa}).setErrorHandler(ua).setServerDialogCancelHandler(va).setRelativeTo(ka).send();}function oa(ta,ua){if(ja){m.hide(ja);}else if(ia)m.hide(ia);ka&&m.hide(ka);la&&m.hide(la);ma&&m.hide(ma);if(ta)m.show(ta);if('Outgoing'==ua&&ha!=ua&&ea)new h(ta).from('backgroundColor','#FFF8CC').to('backgroundColor','transparent').from('borderColor','#FFE222').to('borderColor',s.get(ta,'borderLeftColor')).duration(2000).go();ha&&m.removeClass(v,'fStatus'+ha);ha=ua;m.addClass(v,'fStatus'+ua);}function pa(ta){if(m.hasClass(ta,'enableFriendListFlyout')){o.show(ta);}else o.hide();}var qa=i.subscribe('FriendRequest/change',function(ta,ua){sa();if(ua.uid!=w)return;switch(ua.status){case p.ARE_FRIENDS:return oa(ma,'Friends');case p.INCOMING_REQUEST:return oa(la,'Incoming');case p.OUTGOING_REQUEST:return oa(ka,'Outgoing');case p.CAN_REQUEST:return oa(ja?ja:ia,'Requestable');}}),ra;if(x)ra=i.subscribe('FriendRequest/confirm',function(ta,ua){sa();ua.uid==w&&r(x);});ia&&g.listen(ia,'click',function(){i.inform('FriendRequest/sending',{uid:w});if(ca){o.setActiveNode(ka);}else pa(ka);na("add_friend",function(ta){var ua=ta.error==u.ERROR_ALREADY_ADDED?'FriendRequest/sent':'FriendRequest/sendFail';i.inform(ua,{uid:w});o.hide();k.defaultErrorHandler(ta);},function(ta){i.inform('FriendRequest/sendFail',{uid:w});o.hide();});});function sa(){if(q(ga))return;qa&&qa.unsubscribe();ra&&ra.unsubscribe();qa=ra=null;}}};e.exports=u;});
__d("legacy:FriendStatus",["FriendStatus"],function(a,b,c,d){a.FriendStatus=b('FriendStatus');},3);
__d("FriendButtonIcon",["Arbiter","FriendStatus","Button","arrayContains"],function(a,b,c,d,e,f){var g=b('Arbiter'),h=b('FriendStatus'),i=b('Button'),j=b('arrayContains');e.exports={register:function(k,l,m){g.subscribe('FriendListMembershipChange',function(n,o){if(o.uid==m){var p=j(o.lists,h.CLOSE_FRIENDS),q=j(o.lists,h.ACQUAINTANCES);if(p&&!q){i.setIcon(k,l.close);}else if(q&&!p){i.setIcon(k,l.acquaintance);}else i.setIcon(k,l.friend);}});}};});
__d("legacy:friend-browser-checkbox-js",["FriendBrowserCheckboxController"],function(a,b,c,d){a.FriendBrowserCheckboxController=b('FriendBrowserCheckboxController');},3);
__d("MessageButton",["Chat","Event","MercuryParticipantTypes","copyProperties"],function(a,b,c,d,e,f){var g=b('Chat'),h=b('Event'),i=b('MercuryParticipantTypes'),j=b('copyProperties');function k(){}j(k,{initChat:function(l,m,n){h.listen(l,'click',function(){g.openTab(m,n,i.FRIEND);return false;});}});e.exports=k;});
__d("legacy:onvisible",["OnVisible"],function(a,b,c,d){a.OnVisible=b('OnVisible');},3);