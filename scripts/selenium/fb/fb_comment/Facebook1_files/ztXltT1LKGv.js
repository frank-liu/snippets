/*1361250249,178142511*/

if (self.CavalryLogger) { CavalryLogger.start_js(["tIw4R"]); }

__d("MinNotifications",["Event","Arbiter","AsyncSignal","CSS","Parent","UIPagelet","URI","$","emptyFunction"],function(a,b,c,d,e,f){var g=b('Event'),h=b('Arbiter'),i=b('AsyncSignal'),j=b('CSS'),k=b('Parent'),l=b('UIPagelet'),m=b('URI'),n=b('$'),o=b('emptyFunction'),p=null;function q(){u.fetched=o.thatReturnsTrue;p&&j.removeClass(p,'hasNew');new i(m('/ajax/notifications/mark_read.php').getQualifiedURI().toString(),{seen:1}).send();}function r(){l.loadFromEndpoint('NotificationsJewelPageletController','fbNotificationsList',{},{crossPage:true,handler:q});}var s=n('fbNotificationsList'),t=g.listen(s,'click',function(v){if(window.presenceNotifications){t.remove();return;}var w=k.byTag(v.getTarget(),'li'),x=w&&w.getAttribute('id').replace('notification_','');if(x){j.removeClass(w,'jewelItemNew');new i(m('/ajax/notifications/mark_read.php').getQualifiedURI().toString(),{'alert_ids[0]':x,seen:1}).send();}}),u=a.MinNotifications||{fetchSent:o.thatReturnsFalse,fetched:o.thatReturnsFalse,bootstrap:function(v){u.bootstrap=o;if(window.presenceNotifications)return;p=k.byClass(v,'fbJewel');u.fetchSent=o.thatReturnsTrue;p&&!j.hasClass(p,'hasNew')?r():h.subscribe('fbNotificationsList_wrapper_displayed',q);}};e.exports=u;a.MinNotifications=u;});