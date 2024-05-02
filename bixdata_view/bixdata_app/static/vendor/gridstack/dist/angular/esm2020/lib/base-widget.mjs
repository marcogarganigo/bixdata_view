/**
 * gridstack-item.component.ts 8.2.3
 * Copyright (c) 2022 Alain Dumesny - see GridStack root license
 */
/**
 * Base interface that all widgets need to implement in order for GridstackItemComponent to correctly save/load/delete/..
 */
import { Injectable } from '@angular/core';
import * as i0 from "@angular/core";
export class BaseWidget {
    /**
     * REDEFINE to return an object representing the data needed to re-create yourself, other than `selector` already handled.
     * This should map directly to the @Input() fields of this objects on create, so a simple apply can be used on read
     */
    serialize() { return; }
    /**
     * REDEFINE this if your widget needs to read from saved data and transform it to create itself - you do this for
     * things that are not mapped directly into @Input() fields for example.
     */
    deserialize(w) {
        if (w.input)
            Object.assign(this, w.input);
    }
}
BaseWidget.ɵfac = i0.ɵɵngDeclareFactory({ minVersion: "12.0.0", version: "14.3.0", ngImport: i0, type: BaseWidget, deps: [], target: i0.ɵɵFactoryTarget.Injectable });
BaseWidget.ɵprov = i0.ɵɵngDeclareInjectable({ minVersion: "12.0.0", version: "14.3.0", ngImport: i0, type: BaseWidget });
i0.ɵɵngDeclareClassMetadata({ minVersion: "12.0.0", version: "14.3.0", ngImport: i0, type: BaseWidget, decorators: [{
            type: Injectable
        }] });
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiYmFzZS13aWRnZXQuanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyIuLi8uLi8uLi8uLi9hbmd1bGFyL3Byb2plY3RzL2xpYi9zcmMvbGliL2Jhc2Utd2lkZ2V0LnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBOzs7R0FHRztBQUVIOztHQUVHO0FBRUgsT0FBTyxFQUFFLFVBQVUsRUFBRSxNQUFNLGVBQWUsQ0FBQzs7QUFJMUMsTUFBTSxPQUFnQixVQUFVO0lBQy9COzs7T0FHRztJQUNJLFNBQVMsS0FBZ0MsT0FBTyxDQUFDLENBQUM7SUFFekQ7OztPQUdHO0lBQ0ksV0FBVyxDQUFDLENBQW9CO1FBQ3JDLElBQUksQ0FBQyxDQUFDLEtBQUs7WUFBRyxNQUFNLENBQUMsTUFBTSxDQUFDLElBQUksRUFBRSxDQUFDLENBQUMsS0FBSyxDQUFDLENBQUM7SUFDN0MsQ0FBQzs7dUdBYm9CLFVBQVU7MkdBQVYsVUFBVTsyRkFBVixVQUFVO2tCQUQvQixVQUFVIiwic291cmNlc0NvbnRlbnQiOlsiLyoqXHJcbiAqIGdyaWRzdGFjay1pdGVtLmNvbXBvbmVudC50cyA4LjIuM1xyXG4gKiBDb3B5cmlnaHQgKGMpIDIwMjIgQWxhaW4gRHVtZXNueSAtIHNlZSBHcmlkU3RhY2sgcm9vdCBsaWNlbnNlXHJcbiAqL1xyXG5cclxuLyoqXHJcbiAqIEJhc2UgaW50ZXJmYWNlIHRoYXQgYWxsIHdpZGdldHMgbmVlZCB0byBpbXBsZW1lbnQgaW4gb3JkZXIgZm9yIEdyaWRzdGFja0l0ZW1Db21wb25lbnQgdG8gY29ycmVjdGx5IHNhdmUvbG9hZC9kZWxldGUvLi5cclxuICovXHJcblxyXG5pbXBvcnQgeyBJbmplY3RhYmxlIH0gZnJvbSAnQGFuZ3VsYXIvY29yZSc7XHJcbmltcG9ydCB7IE5nQ29tcElucHV0cywgTmdHcmlkU3RhY2tXaWRnZXQgfSBmcm9tICcuL2dyaWRzdGFjay5jb21wb25lbnQnO1xyXG5cclxuIEBJbmplY3RhYmxlKClcclxuIGV4cG9ydCBhYnN0cmFjdCBjbGFzcyBCYXNlV2lkZ2V0IHtcclxuICAvKipcclxuICAgKiBSRURFRklORSB0byByZXR1cm4gYW4gb2JqZWN0IHJlcHJlc2VudGluZyB0aGUgZGF0YSBuZWVkZWQgdG8gcmUtY3JlYXRlIHlvdXJzZWxmLCBvdGhlciB0aGFuIGBzZWxlY3RvcmAgYWxyZWFkeSBoYW5kbGVkLlxyXG4gICAqIFRoaXMgc2hvdWxkIG1hcCBkaXJlY3RseSB0byB0aGUgQElucHV0KCkgZmllbGRzIG9mIHRoaXMgb2JqZWN0cyBvbiBjcmVhdGUsIHNvIGEgc2ltcGxlIGFwcGx5IGNhbiBiZSB1c2VkIG9uIHJlYWRcclxuICAgKi9cclxuICBwdWJsaWMgc2VyaWFsaXplKCk6IE5nQ29tcElucHV0cyB8IHVuZGVmaW5lZCAgeyByZXR1cm47IH1cclxuXHJcbiAgLyoqXHJcbiAgICogUkVERUZJTkUgdGhpcyBpZiB5b3VyIHdpZGdldCBuZWVkcyB0byByZWFkIGZyb20gc2F2ZWQgZGF0YSBhbmQgdHJhbnNmb3JtIGl0IHRvIGNyZWF0ZSBpdHNlbGYgLSB5b3UgZG8gdGhpcyBmb3JcclxuICAgKiB0aGluZ3MgdGhhdCBhcmUgbm90IG1hcHBlZCBkaXJlY3RseSBpbnRvIEBJbnB1dCgpIGZpZWxkcyBmb3IgZXhhbXBsZS5cclxuICAgKi9cclxuICBwdWJsaWMgZGVzZXJpYWxpemUodzogTmdHcmlkU3RhY2tXaWRnZXQpICB7XHJcbiAgICBpZiAody5pbnB1dCkgIE9iamVjdC5hc3NpZ24odGhpcywgdy5pbnB1dCk7XHJcbiAgfVxyXG4gfVxyXG4iXX0=