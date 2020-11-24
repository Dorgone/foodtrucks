import DS from 'ember-data';

export default DS.Model.extend({
    name: DS.attr(),
    address: DS.attr(),
    longitude: DS.attr(),
    latitude: DS.attr(),
    menu: DS.attr()
});