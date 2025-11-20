#!/usr/bin/env node

// Temporary fix for Node.js v25+ localStorage issue
const { spawn } = require('child_process');
const path = require('path');

// Set the localStorage file path for Node.js v25+
process.env.NODE_OPTIONS = (process.env.NODE_OPTIONS || '') + ' --localstorage-file=/tmp/localstorage-data';

// Start react-scripts
const reactScripts = spawn('node', [
  '--localstorage-file=/tmp/localstorage-data',
  path.join(__dirname, 'node_modules', '.bin', 'react-scripts'),
  'start'
], {
  stdio: 'inherit',
  env: process.env
});

reactScripts.on('close', (code) => {
  process.exit(code);
});

reactScripts.on('error', (err) => {
  console.error('Failed to start react-scripts:', err);
  process.exit(1);
});