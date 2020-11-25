import Controller from '@ember/controller';
import { set } from '@ember/object';

export default Controller.extend({
    actions: {
        toggle: function(foodtruck) { // toggles isOpen property to open or close a food truck info window
            set(foodtruck, 'isOpen', !foodtruck.isOpen); 
        },
    }
});