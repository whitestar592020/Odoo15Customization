/** @odoo-module **/
import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';

var LanguageWidget = Widget.extend({
    template: 'LanguageSystray',

    init: function() {
        this._super.apply(this, arguments);
        var self = this;
        var session = this.getSession();

        self._rpc({
            model: 'res.lang',
            method: 'search_read',
            domain: [['active', '=', true]],
            fields: ['name', 'code', 'iso_code'],
        }).then(function(res){
//            self.$('#language_counter').text(res.length);
            _.each(res, function(lang){
                self.$el.find('#language_list').append('<div class="dropdown-divider"/>');
                if (lang['code'] === session.user_context.lang){
                    self.$el.find('#language_list').append(
                        '<i class="fa fa-circle" style="color: green;"/>&nbsp;'
                    );
                    self.$('#language_counter').text(lang['iso_code']);
                } else {
                    self.$el.find('#language_list').append(
                        '<i class="fa fa-circle" style="color: silver;"/>&nbsp;'
                    );
                }
//                self.$el.find('#language_list').append('<a>' + lang['name'] + '</a>');
                self.$el.find('#language_list').append(
                    '<a data-lang-menu="lang" data-lang-id="' + lang['code'] + '">' + lang['name'] + '</a>'
                );
            });
        });
    },

    start: function(){
        var self = this;
        return this._super.apply(this, arguments).then(function(){
            self.$el.on('click', 'a[data-lang-menu]', function(ev){
                ev.preventDefault();
                var f = self['_changeLanguage'];
                f.call(self, $(this));
            });
        });
    },

    _changeLanguage: function(ev){
        var self = this;
        var lang = $(ev).data("lang-id");
        var session = this.getSession();

        return this._rpc({
            model: 'res.users',
            method: 'write',
            args: [session.uid, {'lang': lang}],
        }).then(function(result){
            self.do_action({
                type: 'ir.actions.client',
                res_model: 'res.users',
                tag: 'reload_context',
                target: 'current',
            });
        });
    },
});

SystrayMenu.Items.push(LanguageWidget);
export default LanguageWidget;
