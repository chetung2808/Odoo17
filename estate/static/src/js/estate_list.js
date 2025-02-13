/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class EstateList extends Component {
    setup() {
        this.orm = useService("orm");
        this.state = useState({ estates: [] });

        onWillStart(async () => {
            this.state.estates = await this.orm.searchRead("estate", [], [
                "name",
                "living_area",
                "garden_area",
                "total_area",
                "state"
            ]);
        });
    }
}

EstateList.template = "test.EstateList";

registry.category("actions").add("test.estate.list", EstateList);
