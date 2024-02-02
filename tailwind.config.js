const Path = require("path");
const pwd = process.env.PWD;


const pySitePackages = process.env.pySitePackages;

// We can add current project paths here
const projectPaths = [
    Path.join(pwd, "./hotwire_django_app/templates/**/*.html"),
    // add js file paths if you need
];

let pyPackagesPaths = []
if (pySitePackages){
    pyPackagesPaths = [
        Path.join(pySitePackages, "./crispy_tailwind/**/*.html"),
        Path.join(pySitePackages, "./crispy_tailwind/**/*.py"),
        Path.join(pySitePackages, "./crispy_tailwind/**/*.js"),
    ];
}

const contentPaths = [...projectPaths, ...pyPackagesPaths];
console.log(`tailwindcss will scan ${contentPaths}`);

module.exports = {
    content: contentPaths,
    theme: {
        extend: {},
    },
    variants: {
        extend: {
            opacity: ['disabled'],
        }
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
}