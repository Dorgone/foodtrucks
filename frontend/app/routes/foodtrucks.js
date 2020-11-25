import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default Route.extend({
    store: service(),
    model() {
        const store = this.get('store');
        return store.findAll('foodtruck'); // returns all of the foodtruck models consumed from the backend API
    }
});